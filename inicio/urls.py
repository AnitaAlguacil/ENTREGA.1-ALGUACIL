  
from django.urls import path
from inicio import views 
  
  
urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('about/', views.about, name = 'about'),
    path('crear-persona/', views.crear_persona, name = 'crear_persona'),            
    path('ver-personas/', views.ver_personas, name = 'ver_personas'), 
        
 ]
  
  
  
