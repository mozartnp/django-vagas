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
        self.assertEqual(resolve(url).func.__name__ , boasvindas_views.boasvindas.__name__, msg="A url não está sendo atendida pela view")

    def test_cadastro_URL_resolve(self):
        '''
        Teste para ver se a URL de cadastro está sendo atendida pela função da view
        '''
        url = reverse('cadastro')
        self.assertEqual(resolve(url).func.__name__ , cadastro_views.cadastro.__name__, msg="A url não está sendo atendida pela view")

    def test_login_URL_resolve(self):
        '''
        Teste para ver se a URL de login está sendo atendida pela função da view
        '''
        url = reverse('login')
        self.assertEqual(resolve(url).func.__name__ , login_views.login.__name__, msg="A url não está sendo atendida pela view")
