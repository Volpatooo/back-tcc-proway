from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model): 
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)


class Profissional(models.Model):
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
