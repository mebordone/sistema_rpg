"""
URL configuration for sistema_rpg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from personajes import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage, name='homepage'),  # Homepage
    path('crear-personaje/', views.crear_personaje, name='crear_personaje'),
    path('ficha-personaje/<int:pk>/', views.ficha_personaje, name='ficha_personaje'),
    path('accounts/', include('django.contrib.auth.urls')),  # Para login/logout
    path('crear/', views.crear_personaje, name='crear_personaje'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    # path('lista/', views.lista_personajes, name='personajes_lista'),
    # path('campanas/', views.lista_campanas, name='campanas_lista'),
    # path('atributos/', views.lista_atributos, name='atributos_lista')
]
