from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Mascota (models.Model):
    nombre = models.CharField (max_length=20)
    tipo = models.CharField (max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo}'
    
    
class Auto (models.Model):
    modelo = models.CharField (max_length=20)
    marca = models.CharField (max_length=20)
    cant_puertas = models.IntegerField()
    color = models.CharField (max_length=20)
    chasis = models.CharField (max_length=20)
    descripcion = RichTextField(null=True)
    
    def __str__(self):
        return f'Modelo: {self.modelo} - Marca: {self.marca} - Chasis: {self.chasis}'