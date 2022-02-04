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
        self.assertEqual(
            resolve(url).func.__name__ ,
            boasvindas_views.boasvindas.__name__ ,
            msg="A url de boas vindas não está sendo atendida pela view"
        )

        # Teste para ver se a pagina retorna o statuts code 200
        self.assertEqual(resposta.status_code, 200)

    ## FIM test_boasvindas_URL_resolve

    def test_cadastro_URL_resolve(self):
        '''
        Teste para ver se a URL de cadastro está sendo atendida pela função da view
        '''
        url = reverse('cadastro')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(
            resolve(url).func.__name__ , 
            cadastro_views.cadastro.__name__, 
            msg="A url cadastro não está sendo atendida pela view"
        )

        # Teste para ver se a pagina retorna o statuts code 200
        self.assertEqual(resposta.status_code, 200)

    ## FIM test_cadastro_URL_resolve

    def test_inserindoCadastro_URL_resolve(self):
        '''
        Teste para ver se a URL de inserindo cadastro está sendo atendida pela função da view
        '''
        url = reverse('inserindoCadastro')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(
            resolve(url).func.__name__ , 
            cadastro_views.inserindoCadastro.__name__, 
            msg="A url de inserindo cadastro não está sendo atendida pela view"
        )
        # Teste para ver se a pagina retorna o statuts code 302, uma vez que a url indica uma view sem template.
        self.assertEqual(resposta.status_code, 302)

    ## FIM test_inserindoCadastro_URL_resolve

    def test_login_URL_resolve(self):
        '''
        Teste para ver se a URL de login está sendo atendida pela função da view
        '''
        url = reverse('login')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(
            resolve(url).func.__name__ , 
            login_views.login.__name__, 
            msg="A url de login não está sendo atendida pela view"
        )

        # Teste para ver se a pagina retorna o statuts code 200
        self.assertEqual(resposta.status_code, 200)

    ## FIM test_login_URL_resolve

    def test_logou_URL_resolve(self):
        '''
        Teste para ver se a URL de logout está sendo atendida pela função da view
        '''
        url = reverse('logout')
        resposta = self.client.get(url)

        # Teste para ver se é atendida pela view
        self.assertEqual(
            resolve(url).func.__name__ , 
            login_views.logout.__name__, 
            msg="A url de logout não está sendo atendida pela view"
        )

        # Para verificar se view esta com o status code correto
        self.assertEqual(
            resposta.status_code,
            302,
            msg='O status code da url logout está errado, deveria ser 302, pois ela é redirecionada.'
        )

    ## FIM test_logou_URL_resolve