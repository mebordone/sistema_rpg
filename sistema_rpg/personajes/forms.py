# personajes/forms.py
from django import forms
from .models import Personaje
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['nombre', 'clase', 'nivel', 'puntos_golpe_max', 'sistema']
        widgets = {
            'sistema': forms.Select(attrs={'class': 'form-select'}),
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

