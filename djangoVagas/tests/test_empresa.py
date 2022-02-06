import time

from django.test import LiveServerTestCase, Client
from selenium import webdriver
from django.urls import reverse
from django.contrib.auth import hashers

from website.escolhas.escolha_escolaridade import NivelEscolaridade
from website.escolhas.escolha_salario import FaixaSalario

from candidato.models.perfil_models import PerfilModel

from empresa.models.info_model import InfoModel

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

        self.empresa_com_info = User.objects.create(
            email= "empresario666@serio.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_com_info.password = hashers.make_password(self.empresa_com_info.password)
        self.empresa_com_info.save()

        self.info_empresa = InfoModel.objects.create(
            nome_empresa= "Criando sonhos",
            telefone_empresa= "(81) 1.1234-8765",
            contato_empresa= "Marcelinho",
            user_id= self.empresa_com_info.id,
        )

        ## FIM empresa_com_info

        self.candidato_com_perfil = User.objects.create(
            email= "ehele@bol.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.candidato_com_perfil.password = hashers.make_password(self.candidato_com_perfil.password)
        self.candidato_com_perfil.save()

        self.info_ehele = PerfilModel.objects.create(
            nome_candidato= "Eh ele",
            telefone_candidato= "(81) 9.9999-9999",
            faixa_salario= "<1k_2k>",
            nivel_escolaridade= "doutorado",
            experiencia= "Tudo e um pouco mais.",
            user_id= self.candidato_com_perfil.id,
        )

        ## FIM candidato_com_perfil
        
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
            self.live_server_url + '/empresa/visualizandoinfo', 
            msg='A pagina de visualização de informações não foi possivel alcançar, vindo de cadastro info.'
        )


    ## FIM test_criando_info_empresa

    def test_candidado_acessando_criando_info_empresa(self):
        ''' 
        Teste de usuario candidato entra na pagina errada cadastrando info da empresa, deve ser redirecinonada
        '''
        # Para logar o selenium na pagina. 
        self.c.login(email=self.candidato_com_perfil.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/cadastrandoinfo')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/cadastrandoinfo')
        
        # Entra na pagina de cadastrar informações da empresa
        # É redirecionado para o login       
        self.assertNotEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='O usuario candidao não está sendo redirecionado na url /empresa/cadastrandoinfo.'
        )

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/', 
            msg='O usuario candidato deveria ser redirecionado para a url /, vindo de /empresa/cadastrandoinfo.'
        )

        # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
        self.assertEqual(
            self.browser.title ,
            'Django Vagas',
            msg='O titulo da pagina não condiz com "Django Vagas".'
        )

    ## FIM test_candidado_acessando_criando_info_empresa

    def test_visualizando_info_empresa(self):
        ''' 
        Teste funcional de usuario empresa visualizando informações
        '''
        # Para logar o selenium na pagina. 
        self.c.login(
            email=self.empresa_com_info.email, 
            password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:'
        )
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/visualizandoinfo')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/visualizandoinfo')

        # Entra na pagina de visualizar info     
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandoinfo', 
            msg='Foi encontrada outra pagina, e não a url /empresa/visualizandoinfo.'
        )

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Vizualizando suas informações',
            msg='O titulo da pagina não condiz com "Vizualizando suas informações".'
        ) 
        # A pessoa lê a mensagem de boas vindas.
        self.assertEqual(
            self.browser.find_element_by_css_selector('section[data-info="mensagemBoasVisualizandoInfo"').text,
            'Seja bem vindo {}!\nSuas informações adicionais.'.format(InfoModel.objects.get(user_id= self.empresa_com_info.id).nome_empresa),
            msg='A mensagem de boas vindas está errada.'
        )

        # Procura a area onde está as info
        self.assertTrue(self.browser.find_element_by_css_selector('section[data-info="suaInfo"'))

        # E lê as informações        
        self.assertEqual(
            self.browser.find_element_by_css_selector('h4[data-info="seuPerfilNome"').text,
            'Nome da empresa: {}'.format(self.info_empresa.nome_empresa),
            msg='O texto do nome da empresa esta errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('h4[data-info="seuPerfilTelefone"').text,
            'Telefone para contato: {}'.format(self.info_empresa.telefone_empresa),
            msg='O texto do telefone da empresa esta errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('h4[data-info="seuPerfilSalario"').text,
            'Nome do contato da empresa: {}'.format(self.info_empresa.contato_empresa),
            msg='O texto da nome do contato da empresa esta errado.'
        )

    # FIM test_visualizando_info_empresa

    def test_candidado_acessando_visualizando_info_empresa(self):
        ''' 
        Teste de usuario candidato entra na pagina errada, visualizando info da empresa, deve ser redirecinonada
        '''
        # Para logar o selenium na pagina. 
        self.c.login(email=self.candidato_com_perfil.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/visualizandoinfo')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/visualizandoinfo')
        
        # Entra na pagina de visualizar informações da empresa
        # É redirecionado para o login       
        self.assertNotEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandoinfo', 
            msg='O usuario candidao não está sendo redirecionado na url /empresa/visualizandoinfo.'
        )

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/', 
            msg='O usuario candidato deveria ser redirecionado para a url /, vindo de /empresa/visualizandoinfo.'
        )

        # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
        self.assertEqual(
            self.browser.title ,
            'Django Vagas',
            msg='O titulo da pagina não condiz com "Django Vagas".'
        )

    ## FIM test_candidado_acessando_visualizando_info_empresa

    def test_empresa_sem_info_acessando_visualizando_info(self):
        ''' 
        Teste de usuario empresa entra na pagina de visualizar info da empresa, mas não tem info, deve ser redirecinonada
        '''
        # Para logar o selenium na pagina. 
        self.c.login(email=self.empresa_sem_info.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/visualizandoinfo')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/visualizandoinfo')
        
        # Entra na pagina de visualizar informações da empresa
        # É redirecionado para o cadastrando info       
        self.assertNotEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandoinfo', 
            msg='O usuario empresa sem info não está sendo redirecionado na url /empresa/visualizandoinfo.'
        )

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='O usuario empresa sem info deveria ser redirecionado para a url /, vindo de /empresa/visualizandoinfo.'
        )

        # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
        self.assertEqual(
            self.browser.title ,
            'Cadastrando suas informações',
            msg='O titulo da pagina não condiz com "Cadastrando suas informações".'
        )

    ## FIM test_empresa_sem_info_acessando_visualizando_info

    def test_empresa_criando_vaga(self):
        ''' 
        Teste funcional de usuario empresa criando vagas
        '''
        # Para logar o selenium na pagina. 
        self.c.login(
            email=self.empresa_com_info.email, 
            password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:'
        )
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/criandovaga')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/criandovaga')

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Criando Vaga',
            msg='O titulo da pagina não condiz com "Criando Vaga".'
        ) 

        # Procura o form das vagas
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="infoVagaForm"'))

        # E lê o texto       
        self.assertEqual(
            self.browser.find_element_by_css_selector('h3[data-info="textoVagaForm"').text,
            'Crie uma nova vaga',
            msg='O texto do nome da empresa esta errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_nome_vaga"').text,
            'Vaga',
            msg='O texto do campo nome da vaga esta errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_faixa_salario"').text,
            'Faixa salarial da vaga\n---------\nAté R$1.000,00\nEntre R$1.000,00 e R$2.000,00\nEntre R$2.000,00 e R$3.000,00\nAcima de R$3.000,00',
            msg='O texto de indicação do campo seletor do faixa salarial está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_nivel_escolaridade"').text,
            'Nível de escolaridade\n---------\nEnsino fundamental\nEnsino médio\nTecnólogo\nEnsino superior\nPós / MBA / Mestrado\nDoutorado',
            msg='O texto de indicação do campo seletor do nivel escolaridade está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_requisitos"').text,
            'Requisitos para a vaga',
            msg='O texto do campo da requisitos para a vaga esta errado.'
        )

        nome_vaga = self.browser.find_element_by_css_selector('input[id="id_nome_vaga"')
        self.assertEqual(
            nome_vaga.get_attribute('placeholder'),
            "Digite uma descrição breve da vaga.",
            msg='O texto do placeholder do nome da vaga está errado.'
        )

        salario = self.browser.find_element_by_css_selector('select[id="id_faixa_salario"')
        escolaridade = self.browser.find_element_by_css_selector('select[id="id_nivel_escolaridade"')

        requisitos = self.browser.find_element_by_css_selector('textarea[id="id_requisitos"')
        self.assertEqual(
            requisitos.get_attribute('placeholder'),
            'Quais são os requisitos da vaga.',
            msg='O texto do placeholder da requisitos está errado.'
        )

        # E é inserido as informações nos devidos campos
        nome_vaga.send_keys('Desenvolvimento em Pyhton Senior')
        salario = self.browser.find_element_by_css_selector('option[value="<2k_3k>"')
        salario.click()
        escolaridade = self.browser.find_element_by_css_selector('option[value="tecnologo"')
        escolaridade.click()
        requisitos.send_keys('TDD\nPython\nGit\nDjango')
       
        # Procura o botão para concluir a criação da vaga e clica nele
        botaoVaga = self.browser.find_element_by_css_selector('div[data-info="botaoVaga"')
        self.assertEqual(
            botaoVaga.text,
            'Concluir Vaga',
            msg='O texto do botão está errado.'
        )
        botaoVaga.click()

        # E espera ser redirecionado para outra pagina, no caso a vizualização das vagas da empresa
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandosuasvagas', 
            msg='A pagina visualizando vaga não foi alcançada apos cadastrar nova vaga.'
        )

    # FIM test_empresa_criando_vaga

    def test_candidado_acessando_criando_vaga(self):
        ''' 
        Teste de usuario candidato entra na pagina errada, criando vaga, deve ser redirecinonada
        '''
        # Para logar o selenium na pagina. 
        self.c.login(email=self.candidato_com_perfil.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/visualizandosuasvagas')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/visualizandosuasvagas')
        
        # Entra na pagina de visualizar informações da empresa
        # É redirecionado para boas vindas       
        self.assertNotEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandosuasvagas', 
            msg='O usuario candidao não está sendo redirecionado na url /empresa/visualizandosuasvagas.'
        )

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/', 
            msg='O usuario candidato deveria ser redirecionado para a url /, vindo de /empresa/visualizandosuasvagas.'
        )

        # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
        self.assertEqual(
            self.browser.title ,
            'Django Vagas',
            msg='O titulo da pagina não condiz com "Django Vagas".'
        )

    ## FIM test_candidado_acessando_criando_vaga

    def test_empresa_sem_info_acessando_visualizando_vagas(self):
        ''' 
        Teste de usuario empresa entra na pagina de visualizar suas vagas da empresa, mas não tem info, deve ser redirecinonada
        '''
        # Para logar o selenium na pagina. 
        self.c.login(email=self.empresa_sem_info.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url + '/empresa/visualizandosuasvagas')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/empresa/visualizandosuasvagas')
        
        # Entra na pagina de visualizar informações da empresa
        # É redirecionado para o cadastrando info       
        self.assertNotEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandosuasvagas', 
            msg='O usuario empresa sem info não está sendo redirecionado na url /empresa/visualizandosuasvagas.'
        )

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='O usuario empresa sem info deveria ser redirecionado para a url /, vindo de /empresa/visualizandoinfo.'
        )

        # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
        self.assertEqual(
            self.browser.title ,
            'Cadastrando suas informações',
            msg='O titulo da pagina não condiz com "Cadastrando suas informações".'
        )

    ## FIM test_empresa_sem_info_acessando_visualizando_vagas
