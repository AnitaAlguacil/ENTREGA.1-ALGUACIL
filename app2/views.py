from django.shortcuts import redirect, render
from app2.forms import MascotaFormulario
from app2.models import Mascota, Auto

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    
    return render(request, 'app2/ver_mascotas.html', {'mascotas': mascotas})

@login_required
def crear_mascota (request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
           datos = formulario.cleaned_data
           
           mascota = Mascota(
               nombre=datos['nombre'],
               tipo=datos['tipo'], 
               edad = datos ['edad'], 
               fecha_nacimiento = datos ['fecha_nacimiento']
            )
           mascota.save()
           return redirect ('ver_mascotas')
    
        else:
            return render(request, 'app2/crear_mascota.html',{'formulario': formulario})
     
          
    formulario = MascotaFormulario()
    
    return render(request, 'app2/crear_mascota.html',{'formulario': formulario})


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




class ListaAutos(ListView):
    model = Auto
    template_name = 'app2/ver_autos.html'  
    
    
    
    
class CrearAuto(LoginRequiredMixin,CreateView):
    model = Auto
    success_url = '/app2/autos/'
    template_name = 'app2/crear_auto.html'
    fields = ['modelo','marca','cant_puertas', 'color', 'chasis']
    
    
class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    success_url = '/app2/autos/'
    template_name = 'app2/editar_auto.html'
    fields = ['modelo','marca','cant_puertas', 'color','chasis']
    
    
    
    
class EliminarAuto(LoginRequiredMixin,DeleteView):
    model = Auto
    success_url = '/app2/autos/'
    template_name = 'app2/eliminar_auto.html'
    
    
    
# class VerMascotas():