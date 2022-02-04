from django.test import SimpleTestCase
from django.urls import reverse, resolve

from candidato.views import *


class TestPerfilURL(SimpleTestCase):
    ''' 
    Teste das URL do aplicativo Candidato
    '''

    def test_criandoperfil_URL_resolve(self):
        '''
        Teste para ver se a URL do Criando Perfil está sendo atendida pela função da view
        '''
        url = reverse('criandoperfil')
        self.assertEqual(
            resolve(url).func.__name__ , 
            criandoperfil.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_criandoperfil_URL_resolve

    def test_inseridoperfil_URL_resolve(self):
        '''
        Teste para ver se a URL do Inserindo Perfil está sendo atendida pela função da view
        '''
    
        url = reverse('inseridoperfil')
        self.assertEqual(
            resolve(url).func.__name__ , 
            inseridoperfil.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_inseridoperfil_URL_resolve

    def test_visualizandoperfil_URL_resolve(self):
        '''
        Teste para ver se a URL do Visualizando Perfil está sendo atendida pela função da view
        '''
    
        url = reverse('visualizandoperfil')
        self.assertEqual(
            resolve(url).func.__name__ , 
            visualizandoperfil.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_visualizandoperfil_URL_resolve