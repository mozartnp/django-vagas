from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import hashers

from candidato.views import perfil_views

from user.models import *


class TestWebsiteViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create(
            email= "teste@testando.com",
            password= "Apesar de voce, 4m4nh4",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.user.password = hashers.make_password(self.user.password)
        self.user.save()

    def test_criandoperfil_view(self):
        '''
        Teste da view do criando perfil
        '''
        # While para testar tanto logado quanto não logado
        validador = 2
        logado = False
        while validador > 0 :
            if not logado:
                response = self.c.get(reverse('criandoperfil'))

                # Para verificar se o está sendo redirecinada para a url certa. 
                self.assertEqual(response.url, '/login')

                # Para verificar se view esta sendo acessada corretamente, como a view é direcionada, o status code será 302.
                self.assertEqual(response.status_code, 302)
            
            elif logado:
                # Para instanciar e logar
                self.c.login(email=self.user.email, password='Apesar de voce, 4m4nh4')
                response = self.c.get(reverse('criandoperfil'))
                

                # Para verificar se o template que a view usa está certo 
                self.assertTemplateUsed(response ,'candidato/criandoperfil.html')

                # Para verificar se view esta sendo acessada corretamente
                self.assertEqual(response.status_code, 200)
            
            logado = True
            validador -= 1

        