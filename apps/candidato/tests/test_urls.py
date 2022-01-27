from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views.candidato_views import cadastro_candidato


class TestCadastroCandidatoURL(SimpleTestCase):
    ''' 
    Teste das URL do aplicativo Candidato
    '''

    def test_cadasto_candidato_URL_resolve(self):
        '''
        Teste para ver se a URL do Cadastro Candidato está sendo atendida pela função da view
        '''

        url = reverse('cadastro_candidato')
        self.assertEqual(resolve(url).func.__name__ , cadastro_candidato.__name__, msg="A url não está sendo atendida pela view")