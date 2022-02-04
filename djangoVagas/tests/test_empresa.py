import time

from django.test import LiveServerTestCase, Client
from selenium import webdriver
from django.urls import reverse
from django.contrib.auth import hashers

from website.models.escolha_escolaridade import *
from website.models.escolha_salario import *

from candidato.models.perfil_models import PerfilModel

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

        ## FIM empresa_criando_info

        self.empresa_sem_info = User.objects.create(
            email= "hacker@russo.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_sem_info.password = hashers.make_password(self.empresa_sem_info.password)
        self.empresa_sem_info.save()

        ## FIM empresa_sem_info

        self.user_com_perfil = User.objects.create(
            email= "ehele@bol.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.user_com_perfil.password = hashers.make_password(self.user_com_perfil.password)
        self.user_com_perfil.save()

        self.info_ehele = PerfilModel.objects.create(
            nome_candidato= "Eh ele",
            telefone_candidato= "(81) 9.9999-9999",
            faixa_salario= "<1k_2k>",
            nivel_escolaridade= "doutorado",
            experiencia= "Tudo e um pouco mais.",
            user_id= self.user_com_perfil.id,
        )
        
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

        # Entra na pagina de criar o cadastrando info     
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='Foi encontrada outra pagina, e não a url /empresa/cadastrandoinfo.'
        )

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Cadastrando suas informações',
            msg='O titulo da pagina não condiz com "Cadastrando suas informações".'
        ) 
 
        # A pessoa vê o aviso e lê.
        self.assertEqual(
            self.browser.find_element_by_css_selector('section[data-info="cadastroInfoAviso"').text,
            'Para poder aproveitar nossa plataforma conclua o cadastro.',
            msg='O aviso está diferente do definido.'
        )

        # E então vai concluir o cadastro.
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="infoEmpresaForm'))
        self.assertEqual(
            self.browser.find_element_by_css_selector('h3[data-info="textoInfoForm').text,
            'Informações Adicionais',
            msg='O texto titulo do formulario em cadastrando info está errado.'
        )
        
        # Procura os campos nome da empresa, telefone da empresa e contato da empresa.
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_nome_empresa"').text,
            'Nome da empresa',
            msg='O texto de indicação do campo nome da empresa está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_telefone_empresa"').text,
            'Telefone para contato',
            msg='O texto de indicação do campo telefone empresa está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_contato_empresa"').text,
            'Nome do contato',
            msg='O texto de indicação do campo contato empresa está errado.'
        )

        nome = self.browser.find_element_by_css_selector('input[id="id_nome_empresa"')
        self.assertEqual(
            nome.get_attribute('placeholder'),
            'Digite o nome da empresa.',
            msg='O texto do placeholder do nome está errado.'
        )

        telefone = self.browser.find_element_by_css_selector('input[id="id_telefone_empresa"')
        self.assertEqual(
            telefone.get_attribute('placeholder'),
            'Digite um telefone com DDD para contato.',
            msg='O texto do placeholder do telefone está errado.'
        )

        contato = self.browser.find_element_by_css_selector('input[id="id_contato_empresa"')
        self.assertEqual(
            contato.get_attribute('placeholder'),
            'Digite o nome de uma pessoa para contato.',
            msg='O texto do placeholder de nome do contato está errado.'
        )

        # E insere as informações necessarias
        nome.send_keys('Cip Vei de Guerra')
        telefone.send_keys('(081) 9.8765-4321')
        contato.send_keys('Bubble')

        # Procura o botão para concluir o cadastro e clica nele
        botaoInfo = self.browser.find_element_by_css_selector('div[data-info="botaoInfo"')
        self.assertEqual(
            botaoInfo.text,
            'Concluir Cadastro',
            msg='O texto do botão está errado.'
        )
        botaoInfo.click()

        # E espera ser redirecionado para outra pagina, no caso a vizualização do perfil dele
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizainfo', 
            msg='A pagina de visualização de informações não foi possivel alcançar, vindo de cadastro info.'
        )


    ### FIM test_criando_info_empresa

    # def test_candidado_acessando_criando_info_empresa(self):
    #     ''' 
    #     Teste de usuario candidato entra na pagina errada cadastrando info da empresa, deve ser redirecinonada
    #     '''
    #     # Para logar o selenium na pagina. 
    #     self.c.login(email=self.user_com_perfil.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
    #     cookie = self.c.cookies['sessionid']
    #     self.browser.get(self.live_server_url + '/empresa/cadastrandoinfo')
    #     self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    #     self.browser.refresh()
    #     self.browser.get(self.live_server_url + '/empresa/cadastrandoinfo')
        
    #     # Entra na pagina de cadastrar informações da empresa
    #     # É redirecionado para o login       
    #     self.assertNotEqual(
    #         self.browser.current_url,
    #         self.live_server_url + '/empresa/cadastrandoinfo', 
    #         msg='O usuario candidao não está sendo redirecionado na url /empresa/cadastrandoinfo.'
    #     )

    #     self.assertEqual(
    #         self.browser.current_url,
    #         self.live_server_url + '/', 
    #         msg='O usuario candidato deveria ser redirecionado para a url /, vindo de /empresa/cadastrandoinfo.'
    #     )

    #     # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
    #     self.assertEqual(
    #         self.browser.title ,
    #         'Django Vagas',
    #         msg='O titulo da pagina não condiz com "Django Vagas".'
    #     )

    # ## FIM test_candidado_acessando_criando_info_empresa

