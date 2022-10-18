from contextvars import Context
from datetime import datetime
import random
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect

import random
from app1.forms import PersonaFormulario, BusquedaPersonaFormulario

from app1.models import Persona



def hola (request):
    return HttpResponse('<h1> Esto es nuevo</h1> ')

def fecha (request):
    fecha_actual =  datetime.now()
    
    return HttpResponse(f'La fecha actual es {fecha_actual}')

def mi_template(request):
    cargar_archivo = open (r'C:\Users\analu\OneDrive\Documentos\ENTREGA.1-ALGUACIL\entregaAlguacil\templates\template1.html', 'r')
    template = Template (cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    template_renderizado = template.render(contexto)
    
    
    return HttpResponse(template_renderizado)



# def tu_template(request, nombre):    
   
#     template = loader.get_template('tu_template.html')
#     template_renderizado = template.render({'persona':nombre})
    
    
#     return HttpResponse(template_renderizado)


def crear_persona(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST) 
        
        if formulario.is_valid():  
            data = formulario.cleaned_data      
        
            nombre = data ['nombre']
            apellido = data ['apellido']
            edad = data ['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now())
            
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion= fecha_creacion)
            persona.save()  
        
            return redirect('ver_personas')
    
    formulario = PersonaFormulario()
             
    return render(request, 'app1/crear_persona.html', {'formulario' : formulario})

 

def ver_personas(request):
    
    nombre =request.GET.get('nombre')
    
    if nombre: 
        personas = Persona.objets.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()        
    
      
    formulario = BusquedaPersonaFormulario()  
    
    return render(request, 'app1/ver_personas.html', {'personas': personas, 'Formulario': formulario})


def index (request):
    
    return render (request, 'app1/index.html' )


def about (request):
    
    return render (request, 'app1/about.html' )