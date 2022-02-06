from django.urls import path 
from .views.info_views import cadastrandoinfo, inseridoinfo, visualizandoinfo
from .views.vaga_views import criandovaga, inserindovaga, visualizandosuasvagas

urlpatterns = [
    path('cadastrandoinfo', cadastrandoinfo, name='cadastrandoinfo'),
    path('inseridoinfo', inseridoinfo, name='inseridoinfo'),
    path('visualizandoinfo', visualizandoinfo, name='visualizandoinfo'),
    path('criandovaga', criandovaga, name='criandovaga'),
    path('inserindovaga', inserindovaga, name='inserindovaga'),
    path('visualizandosuasvagas', visualizandosuasvagas, name='visualizandosuasvagas'),
]