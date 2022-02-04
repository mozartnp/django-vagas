from django.shortcuts import render, redirect

from website.views.login_views import *
from website.models.escolha_escolaridade import *
from website.models.escolha_salario import *

from candidato.forms.perfil_forms import PerfilForm
from candidato.models.perfil_models import PerfilModel

from user.models import User

def criandoperfil(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:

        form_perfil = PerfilForm()

        contexto={
            'form_perfil' : form_perfil,
        }

        return render(request, 'candidato/criandoperfil.html', contexto)
    else:
        return redirect (login)

def inseridoperfil(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:

        if request.POST:
            form = PerfilForm(request.POST)

            if form.is_valid():
                
                objeto = form.save(commit=False)
                user = request.user
                objeto.user = user
                objeto.save()

            return redirect(visualizandoperfil)
    else:
        return redirect (login)

def visualizandoperfil(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        contexto = {}
  
        if request.user.tipo_user == "CAND":
            # Para ver se o usuario já tem um perfil, caso não será redirecionado para a tela de criar perfil
            id_user = request.user.id
            try:
                perfil = PerfilModel.objects.get(user_id=id_user)
                salario = FaixaSalario(perfil.faixa_salario).label
                escolaridade = NivelEscolaridade(perfil.nivel_escolaridade).label

                contexto= {
                    "perfil" : perfil,
                    "salario" : salario,
                    "escolaridade" : escolaridade,
                }
                return render(request, 'candidato/visualizandoperfil.html', contexto)

            except PerfilModel.DoesNotExist:
                return redirect (criandoperfil)

        else:
            return redirect(login) # TODO arrumar para a rota das paginas da empresa
    
    else:
        return redirect (login) 