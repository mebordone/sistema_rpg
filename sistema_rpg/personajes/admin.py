from django.contrib import admin

# Register your models here.
from .models import Personaje, SistemaDeJuego

admin.site.register(Personaje)
admin.site.register(SistemaDeJuego)