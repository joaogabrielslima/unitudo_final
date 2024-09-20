from django.db import models


class Estabelecimento(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=100)
    user_liked = models.BooleanField()
    user_disliked = models.BooleanField()
