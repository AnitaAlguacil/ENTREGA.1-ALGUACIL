from unittest.util import _MAX_LENGTH
from django.db import models


class Persona (models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Nombre y Apellido:{self.nombre} {self.apellido}'
    
    