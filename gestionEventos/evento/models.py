from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()