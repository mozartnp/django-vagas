from django.test import SimpleTestCase
from django.urls import reverse, resolve

from empresa.views.info_views import *


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
