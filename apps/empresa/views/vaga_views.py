from django.shortcuts import render, redirect

from website.models.escolha_escolaridade import *
from website.models.escolha_salario import *
from website.views.login_views import *

from empresa.models.info_model import InfoModel
from empresa.models.vaga_model import VagaModel
from empresa.forms.vaga_form import VagaForm

def criandovaga(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 

            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                InfoModel.objects.get(user_id=request.user.id)
                
                form_vaga = VagaForm()
                contexto={'form_vaga' : form_vaga}

                return render(request, 'empresa/criandovaga.html', contexto)

            except InfoModel.DoesNotExist:
                from empresa.views.info_views import cadastrandoinfo
                return redirect (cadastrandoinfo)    

        elif request.user.tipo_user == ('CAND'):

            #Não pode ser um late import, se não vai da erro de circular imports
            from website.views.boasvindas_views import boasvindas
            return redirect(boasvindas)

    return redirect (login)

def inserindovaga(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:

        if request.POST:
            form = VagaForm(request.POST)

            if form.is_valid():
                
                objeto = form.save(commit=False)
                user = request.user
                objeto.user = user
                objeto.save()

            return redirect(visualizandosuasvagas)

    return redirect (login)
    
def visualizandosuasvagas(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 

            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                InfoModel.objects.get(user_id=request.user.id)

                # Para ver se o usuario tem uma vaga cadastrada
                try:
                    suasvagas = VagaModel.objects.get(user_id=request.user.id)
                    
                    contexto={'suasvagas' : suasvagas}

                except VagaModel.DoesNotExist:
                    suasvagas = False
                    
                    contexto={'suasvagas' : suasvagas}

                return render(request, 'empresa/visualizandosuasvagas.html', contexto)

            except InfoModel.DoesNotExist:
                from empresa.views.info_views import cadastrandoinfo
                return redirect (cadastrandoinfo)    

        elif request.user.tipo_user == ('CAND'):

            #Não pode ser um late import, se não vai da erro de circular imports
            from website.views.boasvindas_views import boasvindas
            return redirect(boasvindas)

    return redirect (login)