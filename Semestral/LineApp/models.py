from django.db import models

# Create your models here.
class Usuario (models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Id del usuario")
    nick = models.CharField(max_length=20,blank=False,null=False,verbose_name="Nickname de usuario")
    foto = models.ImageField(upload_to="avatars",null=True,verbose_name="Foto de perfil")
    correo = models.CharField(max_length=100,blank=False,null=False,verbose_name="Correo electronico del usuario")
    contra = models.CharField(max_length=20,blank=False,null=False,verbose_name="Contraseña del usuario")

    def __str__(self):
        return self.nick

class Lineup (models.Model):
    idLine = models.AutoField(primary_key=True, verbose_name="Id del line up")
    titulo = models.CharField(max_length=50,blank=False,null=False,verbose_name="Titulo del line up")
    agente = models.CharField(max_length=30,blank=False,null=False,verbose_name="Agente del line up")
    mapa = models.CharField(max_length=30,blank=False,null=False,verbose_name="Mapa del line up")
    bando = models.CharField(max_length=3,blank=False,null=False,verbose_name="Bando del line up")
    descripcion = models.CharField(max_length=200,blank=False,null=False,verbose_name="Descripcion del line up")
    incorporacion = models.CharField(max_length=200,blank=False,null=False,verbose_name="Incorporacion del line up")
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

