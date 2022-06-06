from django.contrib import admin
from django.urls import path
from .views import CustomLoginView,inicio,AcercaDe,config,perfil,ranking,registro,subirvideo,editarperfil,listar,eliminar_video, act_perfil, editarVideo, act_video, v_perfil, m_perfil, filtroAgen, filtroMapa, filtroBando
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',inicio,name="inicio"),
    path('filtroAgen/<str:agen>',filtroAgen,name="filtroAgen"),
    path('filtroMapa/<str:mapa>',filtroMapa,name="filtroMapa"),
    path('filtroBando/<int:band>',filtroBando,name="filtroBando"),
    path('AcercaDe/',AcercaDe,name="AcercaDe"),
    path('config/',config,name="config"),
    path('perfil/',perfil,name="perfil"),
    path('v_perfil/',v_perfil,name="v_perfil"),
    path('m_perfil/',m_perfil,name="m_perfil"),
    path('ranking/',ranking,name="ranking"),
    path('registro/',registro,name="registro"),
    path('subirvideo/',login_required(subirvideo),name="subirvideo"),
    path('editarVideo/<int:idLine>',login_required(editarVideo),name="editarVideo"),
    path('act_video/<int:idLine>',login_required(act_video),name="act_video"),
    path('editarperfil/',editarperfil,name="editarperfil"),
    path('act_perfil/',act_perfil,name="act_perfil"),
    path('listar/',listar,name="listar"),
    path('eliminar_video/<int:idLine>',eliminar_video,name="eliminar_video"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='LineApp/inicio.html'), name='logout'),
]