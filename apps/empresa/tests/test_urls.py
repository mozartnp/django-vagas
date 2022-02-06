from django.test import SimpleTestCase
from django.urls import reverse, resolve

from empresa.views.info_views import *
from empresa.views.vaga_views import *


class TestInfolURL(SimpleTestCase):
    ''' 
    Teste das URL relaciondas a Info da empresa
    '''

    def test_cadastrandoinfo_URL_resolve(self):
        '''
        Teste para ver se a URL do Cadastrando Info está sendo atendida pela função da view
        '''
        url = reverse('cadastrandoinfo')
        self.assertEqual(
            resolve(url).func.__name__ , 
            cadastrandoinfo.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_cadastrandoinfo_URL_resolve
    
    def test_inseridoinfo_URL_resolve(self):
        '''
        Teste para ver se a URL do Inserindo Informações está sendo atendida pela função da view
        '''
    
        url = reverse('inseridoinfo')
        self.assertEqual(
            resolve(url).func.__name__ , 
            inseridoinfo.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_inseridoinfo_URL_resolve

    def test_visualizainfo_URL_resolve(self):
        '''
        Teste para ver se a URL de visualizando Informações está sendo atendida pela função da view
        '''
    
        url = reverse('visualizandoinfo')
        self.assertEqual(
            resolve(url).func.__name__ , 
            visualizandoinfo.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_visualizainfo_URL_resolve

    def test_criandovaga_URL_resolve(self):
        '''
        Teste para ver se a URL de criando vaga está sendo atendida pela função da view
        '''
    
        url = reverse('criandovaga')
        self.assertEqual(
            resolve(url).func.__name__ , 
            criandovaga.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_criandovaga_URL_resolve

    def test_inserindovaga_URL_resolve(self):
        '''
        Teste para ver se a URL de inserindo vaga está sendo atendida pela função da view
        '''
    
        url = reverse('inserindovaga')
        self.assertEqual(
            resolve(url).func.__name__ , 
            inserindovaga.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_inserindovaga_URL_resolve

    def test_visualizandosuasvagas_URL_resolve(self):
        '''
        Teste para ver se a URL de visualizando suas vagas está sendo atendida pela função da view
        '''
    
        url = reverse('visualizandosuasvagas')
        self.assertEqual(
            resolve(url).func.__name__ , 
            visualizandosuasvagas.__name__, 
            msg="A url não está sendo atendida pela view"
        )

    ## FIM test_visualizandosuasvagas_URL_resolve