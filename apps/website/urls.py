from django.urls import path 
from .views import *

urlpatterns = [
    path('', boasvindas, name='boasvindas'),
    path('cadastro', cadastro, name='cadastro'),
    path('inserindoCadastro', inserindoCadastro, name='inserindoCadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]