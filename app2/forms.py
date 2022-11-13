from django import forms
from ckeditor.fields import RichTextFormField

class MascotaFormulario(forms.Form):
    nombre = forms.CharField (max_length=20)
    tipo = forms.CharField (max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    

class Auto (forms.Form):
    modelo = forms.CharField (max_length=20)
    marca = forms.CharField (max_length=20)
    cant_puertas = forms.IntegerField()
    color = forms.CharField (max_length=20)
    chasis = forms.CharField (max_length=20)
    descripcion = RichTextFormField(required=False)
    
class BusquedaAutos(forms.Form):
    chasis = forms.CharField(max_length=20, required=False)
    