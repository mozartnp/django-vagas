from django.urls import path 
from .views import *

urlpatterns = [
    path('cadastrocandidato', cadastro_candidato, name='cadastro_candidato'),
]