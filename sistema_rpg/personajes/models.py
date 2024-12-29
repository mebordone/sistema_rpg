# personajes/models.py
from django.contrib.auth.models import User
from django.db import models

class SistemaDeJuego(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=50)
    nivel = models.PositiveIntegerField(default=1)
    puntos_golpe_max = models.PositiveIntegerField(default=10)
    sistema = models.ForeignKey(SistemaDeJuego, on_delete=models.CASCADE)
    jugador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre