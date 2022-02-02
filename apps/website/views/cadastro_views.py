from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

from user.models import User
from user.forms import CadastroUser

from website.views.boasvindas_views import *

from candidato.views.perfil_views import *

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

            return redirect(criandoperfil)

    return redirect(cadastro)