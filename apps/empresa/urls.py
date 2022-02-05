from django.urls import path 
from .views.info_views import cadastrandoinfo, inseridoinfo, visualizandoinfo

urlpatterns = [
    path('cadastrandoinfo', cadastrandoinfo, name='cadastrandoinfo'),
    path('inseridoinfo', inseridoinfo, name='inseridoinfo'),
    path('visualizandoinfo', visualizandoinfo, name='visualizandoinfo'),
]