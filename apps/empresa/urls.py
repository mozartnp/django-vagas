from django.urls import path 
from .views.info_views import cadastrandoinfo, inseridoinfo, visualizandoinfo
from .views.vaga_views import criandovaga, inserindovaga, editandovaga, modificandovaga, excluindovaga, visualizandosuasvagas

urlpatterns = [
    path('cadastrandoinfo', cadastrandoinfo, name='cadastrandoinfo'),
    path('inseridoinfo', inseridoinfo, name='inseridoinfo'),
    path('visualizandoinfo', visualizandoinfo, name='visualizandoinfo'),
    path('criandovaga', criandovaga, name='criandovaga'),
    path('inserindovaga', inserindovaga, name='inserindovaga'),
    path('editandovaga/<int:id_vaga>', editandovaga, name='editandovaga'),
    path('modificandovaga/<int:id_vaga>', modificandovaga, name='modificandovaga'),
    path('excluindovaga/<int:id_vaga>', excluindovaga, name='excluindovaga'),
    path('visualizandosuasvagas', visualizandosuasvagas, name='visualizandosuasvagas'),
]