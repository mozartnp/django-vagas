from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as login_auth,
    logout as logout_auth,
    authenticate
)
from .boasvindas_views import boasvindas

from user.forms import AutencicandoUser

def login(request):    
    # If para verificar se o usuario está logado, caso esteja será redirecinado para a tela devida.
    if request.user.is_authenticated:
        
        # If para ver se é empresa ou candidato
        if request.user.tipo_user == ("EMPR"): 
            from empresa.views.info_views import visualizandoinfo
            redirect(visualizandoinfo)
        elif request.user.tipo_user == ("CAND"):
            from candidato.views.perfil_views import visualizandoperfil
            redirect(visualizandoperfil)

    else:
        if request.POST:
            print('1')
            form_login = AutencicandoUser(request.POST)
            print(form_login.errors)
            

            if form_login.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user =  authenticate(request, email=email, password=password)
                print('2')
                print(user)
                
                if user:
                    print('3')
                    login_auth(request, user)
                    print(user.tipo_user)
                    # If para ver se é empresa ou candidato
                    if user.tipo_user == ("EMPR"): 
                        from empresa.views.info_views import visualizandoinfo
                        redirect(visualizandoinfo)
                    elif request.user.tipo_user == ("CAND"):
                        from candidato.views.perfil_views import visualizandoperfil
                        redirect(visualizandoperfil)
        else:                            
            form_login = AutencicandoUser()
    contexto = { 'form_login' : form_login }
    return render(request, 'website/login.html', contexto)

def logout(request):
    logout_auth(request)
    return redirect('boasvindas')