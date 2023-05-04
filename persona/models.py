from django.db import models

class Persona(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100),

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido')