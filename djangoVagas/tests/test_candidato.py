from django.test import LiveServerTestCase, Client
from selenium import webdriver

import time

class CandidatoTestCase(LiveServerTestCase):

    #Para setar o navegador
    def setUp(self): 
        self.browser = webdriver.Firefox(executable_path='./geckodriver')

    #Para fechar o navegador
    def tearDown(self):
        self.browser.quit()

    # Testes funcionais colaboradores
    def test_cadastro_novo_candidato(self):
        ''' 
        Teste para cadastrar um novo colaborador
        '''
        # Instaciar o client
        c = Client()

        # Abre a pagina de cadastro do colaborador
        resposta = c.post('/candidato/cadastrocandidato')
        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        self.browser.get(self.live_server_url + '/candidato/cadastrocandidato')

