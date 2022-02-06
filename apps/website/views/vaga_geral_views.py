from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect

from candidato.models.perfil_models import PerfilModel

from empresa.models.info_model import InfoModel
from empresa.models.vaga_model import VagaModel

from website.escolhas.escolha_escolaridade import  NivelEscolaridade
from website.escolhas.escolha_salario import FaixaSalario
from website.models.vaga_geral_model import VagaEscolhida
from website.views.login_views import *

from user.models import User

def todasvagas(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
     
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 
    
            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                InfoModel.objects.get(user_id=request.user.id)
            except InfoModel.DoesNotExist:
                from empresa.views.info_views import cadastrandoinfo
                return redirect (cadastrandoinfo)    

        elif request.user.tipo_user == ('CAND'):
            
            # Para ver se o usuario já tem um perfil, caso não será redirecionado para a tela de criar perfil
            try:
                PerfilModel.objects.get(user_id=request.user.id)
            except PerfilModel.DoesNotExist:
                from candidato.views.perfil_views import criandoperfil
                return redirect (criandoperfil) 
   
        contexto = {}

        todasvagas = VagaModel.objects.all()

        paginator = Paginator(todasvagas, 5)
        page = request.GET.get('page')
        todas_vagas_por_pagina = paginator.get_page(page)
        
        contexto['paginacao'] = todas_vagas_por_pagina
        contexto['todasvagas'] = todas_vagas_por_pagina

        return render(request, 'website/todasvagas.html', contexto)  

    return redirect (login)

def vendovaga(request, id_vaga):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        vaga = get_object_or_404(VagaModel, pk=id_vaga) 
        user_empresa_email =  get_object_or_404(User, pk=vaga.user_id)
        user_empresa_email = user_empresa_email.email
        salario = FaixaSalario(vaga.faixa_salario).label
        escolaridade = NivelEscolaridade(vaga.nivel_escolaridade).label
        concorrentes = VagaEscolhida.objects.filter(vaga_id = id_vaga)

        contexto = {
            'vaga' : vaga,
            'is_criador' : False,
            'is_candidato' : False,
            'user_empresa_email' : user_empresa_email,
            'salario' : salario,
            'escolaridade' : escolaridade,
        }
     
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 
    
            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                info = InfoModel.objects.get(user_id=request.user.id)
                contexto['info'] = info
                if vaga.user_id == request.user.id:
                    contexto['is_criador'] = True

            except InfoModel.DoesNotExist:
                from empresa.views.info_views import cadastrandoinfo
                return redirect (cadastrandoinfo) 
            # Para ver se a empresa que está acessando foi quem criou a vaga


        elif request.user.tipo_user == ('CAND'):
            
            # Para ver se o usuario já tem um perfil, caso não será redirecionado para a tela de criar perfil
            try:
                perfil = PerfilModel.objects.get(user_id=request.user.id)
                for concorrente in concorrentes:
                    print(perfil.id, concorrente.candidato_id)
                    if perfil.id == concorrente.candidato_id:
                        contexto['is_candidato'] = True
                        
            except PerfilModel.DoesNotExist:
                from candidato.views.perfil_views import criandoperfil
                return redirect (criandoperfil) 
    
        return render(request, 'website/vendovaga.html', contexto)  

    return redirect (login)

def concorrervaga(request, id_vaga):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        vaga_obj = get_object_or_404(VagaModel, pk=id_vaga)
        perfil_obj = get_object_or_404(PerfilModel, user_id=request.user.id)

        candidato = perfil_obj.pk
        vaga = vaga_obj.pk
        pontuacao = 0

        # Calculo da pontuação
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

        vaga_salario = vaga_obj.faixa_salario
        vaga_salario = conver_salario[vaga_salario]
        vaga_escolaridade = vaga_obj.nivel_escolaridade
        vaga_escolaridade = conver_escolaridade[vaga_escolaridade]

        candidato_salario = perfil_obj.faixa_salario
        candidato_salario = conver_salario[candidato_salario]
        candidato_escolaridade = perfil_obj.nivel_escolaridade
        candidato_escolaridade = conver_escolaridade[candidato_escolaridade]

        if vaga_salario == candidato_salario:
            pontuacao += 1

        if vaga_escolaridade <= candidato_escolaridade:
            pontuacao += 1
        
        VagaEscolhida.objects.create(candidato=perfil_obj, vaga=vaga_obj, pontuacao=pontuacao)
        return redirect(todasvagas)

    return redirect (login)
