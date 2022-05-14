from django.contrib import admin
from django.urls import path
from .views import inicio,inicio2,inicioadmin,AcercaDe,config,perfil,ranking,registro,subirvideo,InicioSesion

urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio2/',inicio2,name="inicio2"),
    path('inicioadmin/',inicioadmin,name="inicioadmin"),
    path('AcercaDe/',AcercaDe,name="AcercaDe"),
    path('config/',config,name="config"),
    path('perfil/',perfil,name="perfil"),
    path('ranking/',ranking,name="ranking"),
    path('home/',registro,name="registro"),
    path('home/',subirvideo,name="subirvideo"),
    path('InicioSesion/',InicioSesion,name="InicioSesion"),
]