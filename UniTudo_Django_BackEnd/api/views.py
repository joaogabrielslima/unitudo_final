from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        
        if user is not None:
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email já cadastrado.'}, status=400)
        
        user = User.objects.create_user(username=email, first_name=name, email=email, password=password)
        user.save()

        return JsonResponse({'message': 'Registrado com sucesso!'}, status=201)
    
    return JsonResponse({'message': 'Method not allowed'}, status=405)
