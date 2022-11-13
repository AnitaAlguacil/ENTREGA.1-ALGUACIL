from contextvars import Context
from datetime import datetime
import random
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import random
from inicio.forms import PersonaFormulario, BusquedaPersonaFormulario

from inicio.models import Persona



@login_required
def crear_persona(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST) 
        
        if formulario.is_valid():  
            data = formulario.cleaned_data      
        
            nombre = data ['nombre']
            apellido = data ['apellido']
            edad = data ['edad']
            fecha_creacion = data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion = datetime.now()
            
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion= fecha_creacion)
            persona.save()  
        
            return redirect('ver_personas')
    
    formulario = PersonaFormulario()
             
    return render(request, 'inicio/crear_persona.html', {'formulario' : formulario})

 

def ver_personas(request):
    
    nombre =request.GET.get('nombre')
    
    if nombre: 
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()        
    
      
    formulario = BusquedaPersonaFormulario()  
    
    return render(request,'inicio/ver_personas.html',{'personas': personas, 'formulario': formulario})


def index (request):
    
    return render (request,'inicio/index.html' )


def about (request):
    
    return render (request,'inicio/about.html' )