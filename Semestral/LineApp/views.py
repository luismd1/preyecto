from django.shortcuts import render

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
    return render(request,'LineApp/registro.html')

def inicio(request):
    return render(request,'LineApp/inicio.html')

def subirvideo(request):
    return render(request,'LineApp/subirvideo.html')

def InicioSesion(request):
    return render(request,'LineApp/InicioSesion.html')

def editarperfil(request):
    return render(request,'LineApp/editarperfil.html')

