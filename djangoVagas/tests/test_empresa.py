import time

from django.test import LiveServerTestCase, Client
from selenium import webdriver
from django.urls import reverse
from django.contrib.auth import hashers

from website.models.escolha_escolaridade import *
from website.models.escolha_salario import *

from user.models import User

class CandidatoTestCase(LiveServerTestCase):

    #Para setar o navegador
    def setUp(self): 
        self.browser = webdriver.Firefox(executable_path='./geckodriver')

        self.c = Client()

        self.empresa_criando_info = User.objects.create(
            email= "empresario@serio.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_criando_info.password = hashers.make_password(self.empresa_criando_info.password)
        self.empresa_criando_info.save()

        self.empresa_sem_info = User.objects.create(
            email= "hacker@russo.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_sem_info.password = hashers.make_password(self.empresa_sem_info.password)
        self.empresa_sem_info.save()

        # self.user_com_info = User.objects.create(
        #     email= "ehele@bol.com",
        #     password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
        #     tipo_user= "CAND"
        # )
        # # Atualizar o hashers do passaword
        # self.user_com_info.password = hashers.make_password(self.user_com_info.password)
        # self.user_com_info.save()

        # self.info_ehele = infoModel.objects.create(
        #     nome_candidato= "Eh ele",
        #     telefone_candidato= "(81) 9.9999-9999",
        #     faixa_salario= "<1k_2k>",
        #     nivel_escolaridade= "doutorado",
        #     experiencia= "Tudo e um pouco mais.",
        #     user_id= self.user_com_info.id,
        # )
        
    ## FIM setUp

    #Para fechar o navegador
    def tearDown(self):
        self.browser.quit()

    ## FIM tearDown

    def test_criando_info_empresa(self):
        ''' 
        Teste funcional para usuario empresa cadastrar informações
        '''
        # Para logar o selenium na pagina. 
        self.c.login(
            email=self.empresa_criando_info.email, 
            password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:'
        )
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/cadastrandoinfo')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/cadastrandoinfo')
        
        # Entra na pagina de criar o perfil do candidato     
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='Foi encontrada outra pagina, e não a url /empresa/cadastrandoinfo.'
        )

    ### FIM test_criando_info_empresa
