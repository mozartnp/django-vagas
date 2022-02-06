from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from candidato.models.perfil_models import PerfilModel

from website.escolhas.escolha_escolaridade import  NivelEscolaridade
from website.escolhas.escolha_salario import FaixaSalario
from website.views.login_views import *

from empresa.models.info_model import InfoModel
from empresa.models.vaga_model import VagaModel

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