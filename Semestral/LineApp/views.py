from django.shortcuts import render, redirect
from LineApp.models import Usuario, Lineup

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

def f_registro(request):
    nick1 = request.POST['reg-usu']
    correo1 = request.POST['reg-email']
    pass1 = request.POST['reg-pass']

    Usuario.objects.create(nick = nick1, correo = correo1, contra = pass1)

    return redirect('registro')

    # HTML INICIO
def inicio(request):
    data = {"lista":Lineup.objects.all().order_by('idLine')[0:12],"lista2":Lineup.objects.all().order_by('idLine')[13:24],"lista3":Lineup.objects.all().order_by('idLine')[25:36]}
    return render(request,'LineApp/inicio.html',data)

def subirvideo(request):
    return render(request,'LineApp/subirvideo.html')

def f_subirvideo(request):
    titulo1 = request.POST['titul']
    agente1 = request.POST['agente']
    mapa1 = request.POST['mapa']
    bando1 = request.POST['bando']
    descripcion1 = request.POST['descripcion']
    incorporacion1 = request.POST['incorporacion']

    Lineup.objects.create(titulo = titulo1, agente = agente1, mapa = mapa1, bando = bando1, descripcion = descripcion1, incorporacion = incorporacion1)

    return redirect('subirvideo')

def InicioSesion(request):
    return render(request,'LineApp/InicioSesion.html')

def editarperfil(request):
    return render(request,'LineApp/editarperfil.html')