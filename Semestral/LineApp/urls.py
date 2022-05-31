from django.contrib import admin
from django.urls import path
from .views import CustomLoginView, inicio,AcercaDe,config,perfil,ranking,registro,subirvideo,editarperfil, inicioadmin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AcercaDe/',AcercaDe,name="AcercaDe"),
    path('config/',config,name="config"),
    path('perfil/',perfil,name="perfil"),
    path('ranking/',ranking,name="ranking"),
    path('registro/',registro,name="registro"),
    path('subirvideo/',login_required(subirvideo),name="subirvideo"),
    path('editarperfil/',editarperfil,name="editarperfil"),
    path('inicioadmin/',inicioadmin,name="inicioadmin"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='LineApp/inicio.html'), name='logout'),
]