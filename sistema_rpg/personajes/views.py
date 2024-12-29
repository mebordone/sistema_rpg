# personajes/views.py
from django.shortcuts import render, redirect
from .forms import PersonajeForm

from .models import Personaje

def homepage(request):
    return render(request, 'homepage.html')

# Vista para crear un nuevo personaje
def crear_personaje(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PersonajeForm(request.POST)
        if form.is_valid():
            personaje = form.save(commit=False)
            personaje.jugador = request.user
            personaje.save()
            return redirect('ficha_personaje', pk=personaje.pk)
    else:
        form = PersonajeForm()
    return render(request, 'personajes/crear_personaje.html', {'form': form})

# Vista para mostrar la ficha del personaje
def ficha_personaje(request, pk):
    personaje = Personaje.objects.get(pk=pk)
    return render(request, 'personajes/ficha_personaje.html', {'personaje': personaje})

from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de login después de registrar
    else:
        form = RegistroForm()
    return render(request, 'personajes/registro.html', {'form': form})

from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirige a la página de inicio o dashboard
        else:
            # Error de login
            return render(request, 'personajes/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'personajes/login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('homepage')