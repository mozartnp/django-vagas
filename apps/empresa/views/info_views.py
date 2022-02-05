from django.shortcuts import render, redirect

from website.views.login_views import *
from website.models.escolha_escolaridade import *
from website.models.escolha_salario import *

from empresa.forms.info_form import InfoForm
from empresa.models.info_model import InfoModel

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

def inseridoinfo(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:

        if request.POST:
            form = InfoForm(request.POST)

            if form.is_valid():
                
                objeto = form.save(commit=False)
                user = request.user
                objeto.user = user
                objeto.save()

            return redirect(visualizandoinfo)

    return redirect (login)

def visualizandoinfo(request):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
    
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ('EMPR'): 

            # Para ver se o usuario já tem um info, caso não será redirecionado para a tela de cadastrar info
            try:
                id_user = request.user.id
                info = InfoModel.objects.get(user_id=id_user)

                contexto= {"info" : info}

                return render(request, 'empresa/visualizandoinfo.html', contexto)

            except InfoModel.DoesNotExist:
                return redirect (cadastrandoinfo)    

        elif request.user.tipo_user == ('CAND'):

            #Não pode ser um late import, se não vai da erro de circular imports
            from website.views.boasvindas_views import boasvindas    
            return redirect(boasvindas)   
    
    return redirect (login)


