from django.urls import path 
from .views import *

urlpatterns = [
    path('criandoperfil', criandoperfil, name='criandoperfil'),
    path('inseridoperfil', inseridoperfil, name='inseridoperfil'),
    path('visualizandoperfil', visualizandoperfil, name='visualizandoperfil'),
]