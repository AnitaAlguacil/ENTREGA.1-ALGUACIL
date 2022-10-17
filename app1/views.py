from contextvars import Context
from datetime import datetime
import random
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render 

import random

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


def crear_persona(request,nombre,apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento= datetime.now())
    
    persona.save()    
      
    return render(request, 'app1/crear_persona.html', {'persona':persona} )

 

def ver_personas(request):
    
    personas = Persona.objects.all()    
    
    return render(request, 'app1/ver_personas.html', {'personas':personas} )

def index (request):
    
    return render (request, 'app1/index.html' )