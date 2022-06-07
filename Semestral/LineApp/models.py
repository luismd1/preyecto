from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

lista = [(-1,"Seleccionar")]
bando = [(-1,"Seleccionar")
        ,(1,"ATK")
        ,(2,"DEF")]
# Create your models here.
class Lineup (models.Model):
    idLine = models.AutoField(primary_key=True, verbose_name="Id del line up")
    titulo = models.CharField(max_length=50,blank=False,null=False,verbose_name="Titulo del line up")
    agente = models.CharField(max_length=30,blank=False,null=False,verbose_name="Agente del line up")
    mapa = models.CharField(max_length=30,blank=False,null=False,verbose_name="Mapa del line up")
    bando = models.IntegerField(blank=False,null=False,verbose_name="Bando del line up",choices=bando,default=-1)
    descripcion = models.CharField(max_length=200,blank=False,null=False,verbose_name="Descripcion del line up")
    incorporacion = models.CharField(max_length=200,blank=False,null=False,verbose_name="Incorporacion del line up")
    like = models.IntegerField(default=0,verbose_name="Likes del line up")
    dislike = models.IntegerField(default=0,verbose_name="Dislikes del line up")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion", null=True)
    usuario = UserForeignKey(auto_user_add=True, verbose_name="Usuario")

    def __str__(self):
        return self.titulo

class Avatar (models.Model):
    idAvatar = models.AutoField(primary_key=True, verbose_name="Id del Avatar")
    avatar = models.FileField(unique=True,upload_to = "avatars",null= True)
    usuario = UserForeignKey(auto_user_add=True, verbose_name="Usuario")
