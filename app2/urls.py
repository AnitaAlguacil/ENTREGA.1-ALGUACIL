from django.urls import path 
from app2 import views

urlpatterns = [
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id>', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:id>', views.eliminar_mascota, name='eliminar_mascota'),
    
    
    path('autos/', views.ListaAutos.as_view(), name='ver_autos'),
    path('autos/crear/', views.CrearAuto.as_view(), name='crear_auto'),
    path('autos/editar/<int:pk>', views.EditarAuto.as_view(), name='editar_auto'),
    path('autos/eliminar/<int:pk>', views.EliminarAuto.as_view(), name='eliminar_auto'),  
    path('autos/ver/<int:pk>', views.VerAuto.as_view(), name='ver_auto')
]
