from django.shortcuts import render
from user.models import User
from user.forms import CadastroUser

def cadastro(request):
    form_cadastrouser = CadastroUser()

    contexto={
        'form_cadastrouser' : form_cadastrouser,
    }

    return render(request, 'website/cadastro.html', contexto)