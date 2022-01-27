from django.urls import path 
from .views import *

urlpatterns = [
    path('', boasvindas, name='boasvindas'),
    path('cadastro', cadastro, name='cadastro'),
]