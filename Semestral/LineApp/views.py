from email import message
from django.shortcuts import render, redirect
from LineApp.models import Lineup
from django.contrib import messages
from .forms import UserForm, VideoForm
from django.contrib.auth.models import User

def inicio(request):
    return render(request,'LineApp/inicio.html')

def AcercaDe(request):
    return render(request,'LineApp/AcercaDe.html')

def config(request):
    return render(request,'LineApp/config.html')

def perfil(request):
    return render(request,'LineApp/perfil.html')

def ranking(request):
    return render(request,'LineApp/ranking.html')


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if request.user.is_authenticated:
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('inicio')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'LineApp/registro.html', contexto)

    # HTML INICIO
def inicio(request):
    data = {"lista":Lineup.objects.all().order_by('idLine')[0:12],"lista2":Lineup.objects.all().order_by('idLine')[13:24],"lista3":Lineup.objects.all().order_by('idLine')[25:36]}
    return render(request,'LineApp/inicio.html',data)


def subirvideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']
            messages.success(request, f'Video {titulo} creado con exito')
            return redirect('inicio')
    else:
        form = VideoForm()
    
    contexto = { 'form' : form }
    return render(request,'LineApp/subirvideo.html', contexto)

def InicioSesion(request):
    return render(request,'LineApp/InicioSesion.html')

def editarperfil(request):
    return render(request,'LineApp/editarperfil.html')