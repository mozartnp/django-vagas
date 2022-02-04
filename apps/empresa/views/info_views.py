from django.shortcuts import render, redirect

from website.views.login_views import *
from website.models.escolha_escolaridade import *
from website.models.escolha_salario import *

from empresa.forms.info_form import InfoForm

def cadastrandoinfo(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 

            form_info = InfoForm()
            contexto={'form_info' : form_info} 

            return render(request, 'empresa/cadastrandoinfo.html', contexto)

        elif request.user.tipo_user == ('CAND'):

            #Não pode ser um late import, se não vai da erro de circular imports
            from website.views.boasvindas_views import boasvindas
            return redirect(boasvindas)

    return redirect (login)
    
