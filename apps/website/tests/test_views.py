from django.test import TestCase, Client
from django.urls import reverse

from ..views import boasvindas_views, cadastro_views, login_views
from user.models import User

class TestWebsiteViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_boasvindas_view(self):
        '''
        Teste da view da boas vindas
        '''
        response = self.c.get(reverse('boasvindas'))

        # Para verificar se o template que a view usa está certo 
        self.assertTemplateUsed(response ,'website/boasvindas.html')

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(response.status_code, 200)

    def test_cadastro_view(self):
        '''
        Teste da view do cadastro de usuario
        '''
        response = self.c.get(reverse('cadastro'))

        # Para verificar se o template que a view usa está certo 
        self.assertTemplateUsed(response ,'website/cadastro.html')

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        '''
        Teste da view do login
        '''
        response = self.c.get(reverse('login'))

        # Para verificar se o template que a view usa está certo 
        self.assertTemplateUsed(response ,'website/login.html')

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(response.status_code, 200)

    def test_inserindoCadastro_view(self):
        '''
        Teste da view inserindo Cadastro 
        '''
        # TODO Algo de estranho aqui!
        response = self.c.post(
            reverse('inserindoCadastro'),
            {
                'email' : 'gandalf@branco.com',
                'tipo_user' : 'CAND',
                'password1' : 'minas morgul 1 Anel',
                'password1' : 'minas morgul 1 Anel',
            } 
        )

        # Para verificar se view esta sendo redirecionada corretamente
        self.assertEqual(response.status_code, 302)
       