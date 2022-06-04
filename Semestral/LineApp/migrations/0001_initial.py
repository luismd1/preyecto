# Generated by Django 4.0.4 on 2022-06-03 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('idLine', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del line up')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo del line up')),
                ('agente', models.CharField(max_length=30, verbose_name='Agente del line up')),
                ('mapa', models.CharField(max_length=30, verbose_name='Mapa del line up')),
                ('bando', models.IntegerField(choices=[(-1, 'Seleccionar'), (1, 'ATK'), (2, 'DEF')], default=-1, verbose_name='Bando del line up')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion del line up')),
                ('incorporacion', models.CharField(max_length=200, verbose_name='Incorporacion del line up')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creacion')),
                ('usuario', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
