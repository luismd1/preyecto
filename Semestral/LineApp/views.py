from email import message
from django.shortcuts import get_object_or_404, render, redirect
from LineApp.models import Lineup
from django.contrib import messages
from .forms import UserForm, VideoForm,  LoginForm, EditUserForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView



def AcercaDe(request):
    return render(request,'LineApp/AcercaDe.html')

def config(request):
    return render(request,'LineApp/config.html')

def perfil(request):
    data = {"videos": Lineup.objects.filter(usuario=request.user.id).order_by('idLine')[:2]}
    return render(request,'LineApp/perfil.html', data)

def v_perfil(request):
    data = {"videos": Lineup.objects.filter(usuario=request.user.id).order_by('idLine')}
    return render(request,'LineApp/perfil.html', data)

def  m_perfil(request):
    videos = Lineup.objects.filter(usuario=request.user.id).order_by('idLine')
    data ={
        'videos':videos
    }
    return render (request,'LineApp/listar.html',data)

def ranking(request):
    return render(request,'LineApp/ranking.html')


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
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
    data = {"lista":Lineup.objects.all().order_by('idLine')[0:16],"lista2":Lineup.objects.all().order_by('idLine')[17:32]}
    return render(request,'LineApp/inicio.html',data)

def filtro(request, agen):
    data = {"lista": Lineup.objects.filter(agente=agen).order_by('idLine')[:16]}
    return render(request,'LineApp/inicio.html', data)

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

def editarVideo(request,idLine):
    video = Lineup.objects.get(pk=idLine)
    form = VideoForm(instance=video)

    return render(request,'LineApp/editarvideo.html',{'form':form, 'video':video})

def act_video(request,idLine):
    video = Lineup.objects.get(pk=idLine)
    form = VideoForm(request.POST, instance=video)
    if form.is_valid():
        form.save()
        messages.success(request, 'Video actualizado con exito')
        return redirect(to="listar")

def InicioSesion(request):
    return render(request,'LineApp/InicioSesion.html')

def editarperfil(request):
    user = User.objects.filter(id=request.user.id).first()
    form = EditUserForm(instance = user)

    return render(request,'LineApp/editarperfil.html',{'form':form, 'user':user})

def act_perfil(request):
    user = User.objects.get(id=request.user.id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil actualizado con exito')
        return redirect(to="perfil")

def listar(request):
    videos= Lineup.objects.all()
    data ={
        'videos':videos
    }
    return render (request,'LineApp/listar.html',data)

def eliminar_video(request,idLine):
    videos= Lineup.objects.get(pk=idLine)
    videos.delete()
    videos = Lineup.objects.all()
    messages.success(request, 'Video eliminado con exito')
    return redirect(to="listar")
    
class CustomLoginView(LoginView):
    template_name = 'LineApp/InicioSesion.html'
    form_class = LoginForm
