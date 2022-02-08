from django.urls import path 
from .views import *

urlpatterns = [
    path('', boasvindas, name='boasvindas'),
    path('cadastro', cadastro, name='cadastro'),
    path('inserindoCadastro', inserindoCadastro, name='inserindoCadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('perfilCandidato/<int:id_vaga>/<int:id_perfil>', perfilCandidato, name='perfilCandidato'),
    path('vagas/todasvagas', todasvagas, name='todasvagas'),
    path('vagas/vendovaga/<int:id_vaga>', vendovaga, name='vendovaga'),
    path('vagas/concorrervaga/<int:id_vaga>', concorrervaga, name='concorrervaga'),
]