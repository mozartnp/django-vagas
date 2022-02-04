from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

from user.models import User
from user.forms import CadastroUser

def cadastro(request):
    form_cadastrouser = CadastroUser()

    contexto={
        'form_cadastrouser' : form_cadastrouser,
    }
    return render(request, 'website/cadastro.html', contexto)

def inserindoCadastro(request):
    if request.POST:
        form = CadastroUser(request.POST)

        if form.is_valid():

            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            usuario = authenticate(email=email, password=password)
            login_auth(request, usuario)

                       
            #IF para diferenciar entre empresa e candidato
            if request.user.tipo_user == ('EMPR'):
                #Não pode ser um late import, se não vai da erro de circular imports
                from empresa.views.info_views import cadastrandoinfo
                return redirect(cadastrandoinfo)

            elif request.user.tipo_user == ('CAND'):
                #Não pode ser um late import, se não vai da erro de circular imports
                from candidato.views.perfil_views import criandoperfil
                return redirect(criandoperfil)

    return redirect(cadastro)