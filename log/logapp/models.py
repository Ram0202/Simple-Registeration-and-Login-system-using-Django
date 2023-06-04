from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=128)