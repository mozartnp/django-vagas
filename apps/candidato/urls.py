from django.urls import path 
from .views.perfil_views import criandoperfil, inseridoperfil, visualizandoperfil

urlpatterns = [
    path('criandoperfil', criandoperfil, name='criandoperfil'),
    path('inseridoperfil', inseridoperfil, name='inseridoperfil'),
    path('visualizandoperfil', visualizandoperfil, name='visualizandoperfil'),
]