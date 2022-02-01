from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import boasvindas_views, cadastro_views, login_views

class TestWebsiteURL(SimpleTestCase):
    ''' 
    Teste das URL do aplicativo Candidato
    '''

    def test_boasvindas_URL_resolve(self):
        '''
        Teste para ver se a URL de boas vindas está sendo atendida pela função da view
        '''
        url = reverse('boasvindas')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(resolve(url).func.__name__ , boasvindas_views.boasvindas.__name__, msg="A url não está sendo atendida pela view")
        # Teste para ver se a pagina retorna o statuts code 200
        self.assertEqual(resposta.status_code, 200)

    def test_cadastro_URL_resolve(self):
        '''
        Teste para ver se a URL de cadastro está sendo atendida pela função da view
        '''
        url = reverse('cadastro')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(resolve(url).func.__name__ , cadastro_views.cadastro.__name__, msg="A url não está sendo atendida pela view")
        # Teste para ver se a pagina retorna o statuts code 200
        self.assertEqual(resposta.status_code, 200)

    def test_login_URL_resolve(self):
        '''
        Teste para ver se a URL de login está sendo atendida pela função da view
        '''
        url = reverse('login')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(resolve(url).func.__name__ , login_views.login.__name__, msg="A url não está sendo atendida pela view")
        # Teste para ver se a pagina retorna o statuts code 200
        self.assertEqual(resposta.status_code, 200)