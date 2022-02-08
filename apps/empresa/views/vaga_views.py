from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect

from candidato.models.perfil_models import PerfilModel

from empresa.models.info_model import InfoModel
from empresa.models.vaga_model import VagaModel
from empresa.forms.vaga_form import VagaForm

from website.escolhas.escolha_escolaridade import  NivelEscolaridade
from website.escolhas.escolha_salario import FaixaSalario
from website.models.vaga_geral_model import VagaEscolhida
from website.views.login_views import *

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

def editandovaga (request, id_vaga):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
         # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 

            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                InfoModel.objects.get(user_id=request.user.id)
                               
                vaga = VagaModel.objects.get(id=id_vaga)
                form_vaga = VagaForm(instance=vaga)
                contexto={
                    'form_vaga' : form_vaga,
                    'vaga' : vaga,
                }

                return render(request, 'empresa/editandovaga.html', contexto)

            except InfoModel.DoesNotExist:
                from empresa.views.info_views import cadastrandoinfo
                return redirect (cadastrandoinfo) 

        elif request.user.tipo_user == ('CAND'):
            #Não pode ser um late import, se não vai da erro de circular imports
            from website.views.boasvindas_views import boasvindas
            return redirect(boasvindas)   
       
    return redirect (login)

def modificandovaga (request, id_vaga):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:

        if request.POST:
            vaga = VagaModel.objects.get(id=id_vaga)
            form = VagaForm(request.POST, instance=vaga)
            
            if form.is_valid():
                
                objeto = form.save(commit=False)
                objeto.save()

                # Recontagem de pontos quando modifica a vaga
                concorrentes = VagaEscolhida.objects.filter(vaga_id = id_vaga)
                vaga = VagaModel.objects.get(id=id_vaga)
                conver_salario = {
                    '<1k' : 1,
                    '<1k_2k>' : 2,
                    '<2k_3k>' : 3,
                    '>3k' : 4,
                }
                conver_escolaridade = {
                    'fundamental' : 1,
                    'medio' : 2,
                    'tecnologo' : 3,
                    'superior' : 4,
                    'pos' : 5,
                    'doutorado' : 6,
                }
                vaga_salario = vaga.faixa_salario
                vaga_salario = conver_salario[vaga_salario]
                vaga_escolaridade = vaga.nivel_escolaridade
                vaga_escolaridade = conver_escolaridade[vaga_escolaridade]

                for concorrente in concorrentes:
                    pontuacao = 0
                    perfil = PerfilModel.objects.get(pk=concorrente.candidato_id)
                    candidato_salario = perfil.faixa_salario
                    candidato_salario = conver_salario[candidato_salario]
                    candidato_escolaridade = perfil.nivel_escolaridade
                    candidato_escolaridade = conver_escolaridade[candidato_escolaridade]

                    if vaga_salario == candidato_salario:
                        pontuacao += 1

                    if vaga_escolaridade <= candidato_escolaridade:
                        pontuacao += 1

                    concorrente.pontuacao = pontuacao
                    concorrente.save()

            return redirect(visualizandosuasvagas)

    return redirect (login)

def excluindovaga (request, id_vaga):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        vaga = get_object_or_404(VagaModel, pk=id_vaga)
        vaga.delete()

        return redirect(visualizandosuasvagas)

    return redirect (login)
    
def visualizandosuasvagas(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 
            contexto = {}

            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                info = InfoModel.objects.get(user_id=request.user.id)
                contexto['info'] = info

                # Para ver se o usuario tem uma vaga cadastrada
                try:
                    suasvagas = VagaModel.objects.filter(user_id=request.user.id)

                    paginator = Paginator(suasvagas, 5)
                    page = request.GET.get('page')
                    suas_vagas_por_pagina = paginator.get_page(page)
                    
                    contexto['paginacao'] = suas_vagas_por_pagina
                    contexto['suasvagas'] = suas_vagas_por_pagina

                except VagaModel.DoesNotExist:
                    suasvagas = False
                    
                    contexto['suasvagas'] = suasvagas

                return render(request, 'empresa/visualizandosuasvagas.html', contexto)

            except InfoModel.DoesNotExist:
                from empresa.views.info_views import cadastrandoinfo
                return redirect (cadastrandoinfo)    

        elif request.user.tipo_user == ('CAND'):

            #Não pode ser um late import, se não vai da erro de circular imports
            from website.views.boasvindas_views import boasvindas
            return redirect(boasvindas)

    return redirect (login)