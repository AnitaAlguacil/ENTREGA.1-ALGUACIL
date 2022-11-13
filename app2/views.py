from django.shortcuts import redirect, render
from app2.forms import MascotaFormulario, BusquedaAutos, BusquedaMascotas
from app2.models import Mascota, Auto

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def ver_mascotas(request):
    mascota =request.GET.get('mascota')
    
    if mascota: 
        mascotas = Mascota.objects.filter(mascota__icontains=mascota)
    else:
        mascotas = Mascota.objects.all()        
    
      
    formulario = BusquedaMascotas()  
    
    return render(request, 'app2/ver_mascotas.html', {'mascotas': mascotas, 'formulario': formulario})
    
    

@login_required
def crear_mascota (request):
    
    if request.method == 'POST':
        
        formulario = MascotaFormulario(request.POST) 
        
        if formulario.is_valid():  
            data = formulario.cleaned_data      
        
            nombre = data ['nombre']
            tipo = data ['tipo']
            edad = data ['edad']
            fecha_nacimiento = data['fecha_nacimiento']
            
            
            mascota = Mascota(nombre=nombre, tipo=tipo, edad=edad, fecha_nacimiento= fecha_nacimiento)
            mascota.save()  
        
            return redirect('ver_mascotas')
    
    formulario = MascotaFormulario()
             
    return render(request, 'app2/crear_mascota.html', {'formulario' : formulario})


@login_required
def editar_mascota (request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
          
            mascota.nombre=datos['nombre']
            mascota.tipo=datos['tipo']
            mascota.edad= datos ['edad']
            mascota.fecha_nacimiento= datos ['fecha_nacimiento']
        
            mascota.save()
        
            return redirect ('ver_mascotas')
        else:
            return render(request,'app2/editar_mascota.html', {'formulario': formulario})

            
    
    formulario = MascotaFormulario(
        initial= {
            'nombre':mascota.nombre,
            'tipo':mascota.tipo,
            'edad':mascota.edad,
            'fecha_nacimineto':mascota.fecha_nacimiento
        }
    )
    
    return render(request, 'app2/editar_mascota.html',{'formulario': formulario, 'mascota': mascota})
    
@login_required
def eliminar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    
    return redirect('ver_mascotas')


def ver_autos(request):
    
    auto =request.GET.get('auto')
    
    if auto: 
        autos = Auto.objects.filter(auto__icontains=auto)
    else:
        autos = Auto.objects.all()        
    
      
    formulario = BusquedaAutos()  
    
    return render(request, 'app2/ver_autos.html', {'autos': autos, 'formulario': formulario})


def index (request):
    
    return render (request, 'app1/index.html' )


 
class CrearAuto(LoginRequiredMixin,CreateView):
    model = Auto
    success_url = '/app2/autos/'
    template_name = 'app2/crear_auto.html'
    fields = ['modelo','marca','cant_puertas', 'color', 'chasis', 'descripcion']
    
    
class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    success_url = '/app2/autos/'
    template_name = 'app2/editar_auto.html'
    fields = ['modelo','marca','cant_puertas', 'color','chasis', 'descripcion']
    
    
    
    
class EliminarAuto(LoginRequiredMixin,DeleteView):
    model = Auto
    success_url = '/app2/autos/'
    template_name = 'app2/eliminar_auto.html'    

  
    
    
class VerAuto(DetailView):
    model = Auto
    temaplte_name = 'app2/ver_auto.html'

    
    