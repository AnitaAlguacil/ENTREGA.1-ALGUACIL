  
from django.urls import path
from app1 import views 
  
  
urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('hola/', views.hola, name = 'hola'),
    path ('about/', views.about, name = 'about'),
    path('mi-template/', views.mi_template, name = 'mi_template'),
    path('crear-persona/', views.crear_persona, name = 'crear_persona'),            
    path('ver-personas/', views.ver_personas, name = 'ver_personas'), 
    path('about/', views.about, name = 'about')    
     
 ]
  
  
  
