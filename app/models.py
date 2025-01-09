from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model): 
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Profissional(models.Model):
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)
    area_atuacao = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.nome} {self.sobrenome} {(self.area_atuacao)}"


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_profissional = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)
