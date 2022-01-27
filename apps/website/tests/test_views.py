from django.test import TestCase, Client
from django.urls import reverse

from ..views import boasvindas_views, cadastro_views

class TestWebsiteViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_boasvindas_view(self):
        '''
        Teste da view da boas vindas
        '''
        response = self.client.get(reverse('boasvindas'))

        # Para verificar se o template que a view usa está certo 
        self.assertTemplateUsed(response ,'website/boasvindas.html')

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(response.status_code, 200)

    def test_cadastro_view(self):
        '''
        Teste da view do cadastro de usuario
        '''

        response = self.client.get(reverse('cadastro'))

        # Para verificar se o template que a view usa está certo 
        self.assertTemplateUsed(response ,'website/cadastro.html')

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(response.status_code, 200)