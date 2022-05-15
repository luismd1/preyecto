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

# HTML inicio

def inicio(request):
    contexto = {
    "titLineApp":"Nano para verdes de C", 
    "descLineApp":"Nanoenjambre lanzado desde Lobby de Larga para limpiar tras las cajas Verdes de la derecha y frenar el apoyo de garaje",
    "habilidad":"Nanoenjambre",
    "areaLimpieza":"C",
    "videoLineApp":"https://www.youtube.com/embed/d9xGs0jOz1w",
    "imagenAgent":"/static/LineApp/img/Avatar/killjoy.png",
    "fechaVideo":"10/10/2020"}
    return render(request,'LineApp/inicio.html',contexto) 