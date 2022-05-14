from django.contrib import admin
from django.urls import path
from .views import inicio,AcercaDe,config,perfil,ranking,registro,subirvideo,InicioSesion,editarperfil

urlpatterns = [
    path('',inicio,name="inicio"),
    path('AcercaDe/',AcercaDe,name="AcercaDe"),
    path('config/',config,name="config"),
    path('perfil/',perfil,name="perfil"),
    path('ranking/',ranking,name="ranking"),
    path('registro/',registro,name="registro"),
    path('subirvideo/',subirvideo,name="subirvideo"),
    path('InicioSesion/',InicioSesion,name="InicioSesion"),
    path('editarperfil/',editarperfil,name="editarperfil"),
]