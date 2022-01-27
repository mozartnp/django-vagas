from django.test import LiveServerTestCase, Client
from selenium import webdriver

import time

class UsuarioTestCase(LiveServerTestCase):

    #Para setar o navegador
    def setUp(self): 
        self.browser = webdriver.Firefox(executable_path='./geckodriver')

    #Para fechar o navegador
    def tearDown(self):
        self.browser.quit()

    # Testes funcionais do usuario
    def test_pagina_boas_vindas_registro(self):
        ''' 
        Teste da pagina inicial. Onde o usuario vai para o registro.
        '''
        # instanciar o client
        c = Client()

        # A pessoa abre o site do Django Vagas
        resposta = c.post('')
        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        self.browser.get(self.live_server_url + '')

        # Ela confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Django Vagas',
            msg='O titulo da pagina não condiz com "Django Vagas".'
        )

        # A pessoa vê o anuncio e lê.
        anuncio = self.browser.find_element_by_css_selector('section[data-info="boasVindasAnuncio"')
        self.assertEqual(
            anuncio.text,
            'Django Vagas, a maior plataforma de empregos django do Brasil.\n\nSe você está procurando empregos, não perca tempo se cadastre.\nCaso seja uma empresa, cadastre-se e desfrute da nossa base de candidatos.',
            msg='O anuncio está diferente do definido.'
        )

        # Fica interresada e vai se cadastrar.
        cadastro = self.browser.find_element_by_css_selector('div[data-info="botaoCadastro"')
        self.assertEqual(
            cadastro.text,
            'Cadastro',
            msg='O texto do botão de cadastro está errado.'
        )

        #A pessoa clica no botão de cadastro.
        cadastro.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/cadastro', msg='A pagina de cadastro não foi alcançada pelo botão de cadastro.')

    def test_pagina_boas_vindas_login(self):
        '''
        Teste da pagina inicial. Onde o usuario vai para o login.
        '''
        self.browser.get(self.live_server_url + '')
 
        # Ela confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Django Vagas',
            msg='O titulo da pagina não condiz com "Django Vagas".'
        )

         # Fica interresada e vai se cadastrar.
        cadastro = self.browser.find_element_by_css_selector('div[data-info="botaoLogin"')
        self.assertEqual(
            cadastro.text,
            'Login',
            msg='O texto do botão de Login está errado.'
        )

        #A pessoa clica no botão de cadastro. 
        cadastro.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/login', msg='A pagina de login não foi alcançada pelo botão de login.')

        

