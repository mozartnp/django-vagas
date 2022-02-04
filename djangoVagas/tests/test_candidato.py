# import time

# from django.test import LiveServerTestCase, Client
# from selenium import webdriver
# from django.urls import reverse
# from django.contrib.auth import hashers

# from candidato.models.perfil_models import PerfilModel

# from empresa.models.info_model import InfoModel

# from website.models.escolha_escolaridade import *
# from website.models.escolha_salario import *

# from user.models import User

# class CandidatoTestCase(LiveServerTestCase):

#     #Para setar o navegador
#     def setUp(self): 
#         self.browser = webdriver.Firefox(executable_path='./geckodriver')

#         self.c = Client()

#         self.user_criando_perfil = User.objects.create(
#             email= "tibia@fibula.com",
#             password= "J040 e M4R14 querem doce",
#             tipo_user= "CAND"
#         )
#         # Atualizar o hashers do passaword
#         self.user_criando_perfil.password = hashers.make_password(self.user_criando_perfil.password)
#         self.user_criando_perfil.save()

#         ## FIM user_criando_perfil

#         self.user_sem_perfil = User.objects.create(
#             email= "hacker@russo.com",
#             password= "VOU pegar teus d4d0s",
#             tipo_user= "CAND"
#         )
#         # Atualizar o hashers do passaword
#         self.user_sem_perfil.password = hashers.make_password(self.user_sem_perfil.password)
#         self.user_sem_perfil.save()

#         ## FIM user_sem_perfil

#         self.user_com_perfil = User.objects.create(
#             email= "ehele@bol.com",
#             password= "Meteu essa @pocoto 69",
#             tipo_user= "CAND"
#         )
#         # Atualizar o hashers do passaword
#         self.user_com_perfil.password = hashers.make_password(self.user_com_perfil.password)
#         self.user_com_perfil.save()

#         self.perfil_ehele = PerfilModel.objects.create(
#             nome_candidato= "Eh ele",
#             telefone_candidato= "(81) 9.9999-9999",
#             faixa_salario= "<1k_2k>",
#             nivel_escolaridade= "doutorado",
#             experiencia= "Tudo e um pouco mais.",
#             user_id= self.user_com_perfil.id,
#         )

#         ## FIM user_com_perfil

#         self.empresa_com_info = User.objects.create(
#             email= "voando@damulesta.com",
#             password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
#             tipo_user= "EMPR"
#         )
#         # Atualizar o hashers do passaword
#         self.empresa_com_info.password = hashers.make_password(self.empresa_com_info.password)
#         self.empresa_com_info.save()

#         self.info_empresa = InfoModel.objects.create(
#             nome_empresa= "Criando sonhos",
#             telefone_empresa= "(81) 1.1234-8765",
#             contato_empresa= "Marcelinho",
#             user_id= self.empresa_com_info.id,
#         )

#         ## FIM empresa_com_info
    
#     ##FIM setUp        

#     #Para fechar o navegador
#     def tearDown(self):
#         self.browser.quit()

#     ## FIM tearDown
    
#     # Testes funcionais candidato
#     def test_criando_perfil_candidato(self):
#         ''' 
#         Teste para criar um novo perfil, de candidato
#         '''
#         # Para logar o selenium na pagina. 
#         self.c.login(email=self.user_criando_perfil.email, password='J040 e M4R14 querem doce')
#         cookie = self.c.cookies['sessionid']
#         self.browser.get(self.live_server_url + '/candidato/criandoperfil')
#         self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
#         self.browser.refresh()
#         self.browser.get(self.live_server_url + '/candidato/criandoperfil')
        
#         # Entra na pagina de criar o perfil do candidato     
#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/criandoperfil', 
#             msg='Foi encontrada outra pagina, e não a url /candidato/criandoperfil.'
#         )
    
#         # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
#         self.assertEqual(
#             self.browser.title ,
#             'Criando seu perfil',
#             msg='O titulo da pagina não condiz com "Criando seu perfil.".'
#         )

#         # A pessoa vê o aviso.
#         aviso = self.browser.find_element_by_css_selector('section[data-info="avisoPerfilCandidato"')
#         self.assertEqual(
#             aviso.text,
#             'Para poder aproveitar nossas vagas\nVocê precisa preencher o seu perfil.',
#             msg='O aviso está diferente do definido:\nPara poder aproveitar nossas vagas\nVocê precisa preencher o seu perfil.'
#         )

#         # Decide preencher o perfil, para isso procura o formulario
#         self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="perfilCandidatoForm'))
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h3[data-info="textoPerfilForm').text,
#             'Criando seu perfil',
#             msg='O texto titulo do formulario criando perfil está errado.'
#         )

#         # Ao achar o formulario, procura os campos: Nome, Telefone, Salario, Escolaridade e Exeperiencias.
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_nome_candidato"').text,
#             'Seu nome',
#             msg='O texto de indicação do campo nome está errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_telefone_candidato"').text,
#             'Telefone para contato',
#             msg='O texto de indicação do campo telefone está errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_faixa_salario"').text,
#             'Expectativa salarial\n---------\nAté R$1.000,00\nEntre R$1.000,00 e R$2.000,00\nEntre R$2.000,00 e R$3.000,00\nAcima de R$3.000,00',
#             msg='O texto de indicação do campo seletor da faixa salario está errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_nivel_escolaridade"').text,
#             'Nível de escolaridade\n---------\nEnsino fundamental\nEnsino médio\nTecnólogo\nEnsino superior\nPós / MBA / Mestrado\nDoutorado',
#             msg='O texto de indicação do campo seletor do nivel escolaridade está errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_experiencia"').text,
#             'Suas experiências',
#             msg='O texto de indicação do campo experiencia está errado.'
#         )       

#         nome = self.browser.find_element_by_css_selector('input[id="id_nome_candidato"')
#         self.assertEqual(
#             nome.get_attribute('placeholder'),
#             'Digite seu nome completo.',
#             msg='O texto do placeholder do nome está errado.'
#         )

#         telefone = self.browser.find_element_by_css_selector('input[id="id_telefone_candidato"')
#         self.assertEqual(
#             telefone.get_attribute('placeholder'),
#             'Digite um telefone com DDD para contato.',
#             msg='O texto do placeholder do telefone está errado.'
#         )

#         salario = self.browser.find_element_by_css_selector('select[id="id_faixa_salario"')
#         escolaridade = self.browser.find_element_by_css_selector('select[id="id_nivel_escolaridade"')

#         experiencia = self.browser.find_element_by_css_selector('textarea[id="id_experiencia"')
#         self.assertEqual(
#             experiencia.get_attribute('placeholder'),
#             'Fale um pouco sobre suas experiências na área.',
#             msg='O texto do placeholder da experiencia está errado.'
#         )

#         # E é inserido as informações nos devidos campos
#         nome.send_keys('Tibiano Vei de Guerra')
#         telefone.send_keys('(081) 9.8765-4321')
#         salario = self.browser.find_element_by_css_selector('option[value="<2k_3k>"')
#         salario.click()
#         escolaridade = self.browser.find_element_by_css_selector('option[value="tecnologo"')
#         escolaridade.click()
#         experiencia.send_keys('Acho legal fazer site em django.\nJá fiz alguns sitemas online assim.\nE trabalhar usando TDD é mais facil.')

#         # Procura o botão para concluir o cadastro e clica nele
#         botaoPerfil = self.browser.find_element_by_css_selector('div[data-info="botaoPerfil"')
#         botaoPerfil.click()

#         # E espera ser redirecionado para outra pagina, no caso a vizualização do perfil dele
#         time.sleep(1)
#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/visualizandoperfil', 
#             msg='A pagina do perfil do candidato não foi alcançada apos cadastro do perfil.'
#         )

#     ## FIM test_criando_perfil_candidato

#     def test_empresa_acessando_criando_perfil_candidato(self):
#         ''' 
#         Teste de usuario empresa entra na pagina errada criando perfil de candidato, deve ser redirecinonada
#         '''
#         # Para logar o selenium na pagina. 
#         self.c.login(email=self.empresa_com_info.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
#         cookie = self.c.cookies['sessionid']
#         self.browser.get(self.live_server_url + '/candidato/criandoperfil')
#         self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
#         self.browser.refresh()
#         self.browser.get(self.live_server_url + '/candidato/criandoperfil')
        
#         # Entra na pagina de criar o perfil do candidato     
#         self.assertNotEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/criandoperfil', 
#             msg='O usuario empresa não está sendo redirecionado na url /candidato/criandoperfil.'
#         )

#         # Entra na pagina de criar o perfil do candidato     
#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/', 
#             msg='O usuario empresa deveria ser redirecionado na url /.'
#         )

#         # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
#         self.assertEqual(
#             self.browser.title ,
#             'Django Vagas',
#             msg='O titulo da pagina não condiz com "Django Vagas".'
#         )

#     ## FIM test_empresa_acessando_criando_perfil_candidato

#     def test_visualizar_perfil_candidato(self):
#         ''' 
#         Teste para vaizualizar o perfil do candidato.
#         '''
#         # Para logar o selenium na pagina. 

#         self.c.login(email=self.user_com_perfil.email, password='Meteu essa @pocoto 69')
#         cookie = self.c.cookies['sessionid']
#         self.browser.get(self.live_server_url + '/candidato/visualizandoperfil')
#         self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
#         self.browser.refresh()
#         self.browser.get(self.live_server_url + '/candidato/visualizandoperfil')

#         # Entra na pagina de vizualizar perfil.     
#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/visualizandoperfil', 
#             msg='Foi encontrada outra pagina, e não a url /candidato/visualizandoperfil.'
#         )

#         # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
#         self.assertEqual(
#             self.browser.title ,
#             'Vizualizando seu perfil',
#             msg='O titulo da pagina não condiz com "Vizualizando seu perfil.".'
#         )        

#         # Uma vez dentro da pagina ele vizualiza a sidebar
#         self.assertTrue(self.browser.find_element_by_css_selector('nav[data-info="navSideBar'))

#         # A pessoa lê a mensagem de boas vindas.
#         aviso = self.browser.find_element_by_css_selector('section[data-info="mensagemBoasvisualizandoperfil"')
#         self.assertEqual(
#             aviso.text,
#             'Olá {}!\nEste é o seu perfil.'.format(PerfilModel.objects.get(user_id= self.user_com_perfil.id).nome_candidato),
#             msg='A mensagem de boas vindas está errada.'
#         )

#         # Procura a area onde está o perfil
#         self.assertTrue(self.browser.find_element_by_css_selector('section[data-info="seuPerfil"'))

#         # E lê as informações        
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h4[data-info="seuPerfilNome"').text,
#             'Seu nome: {}'.format(self.perfil_ehele.nome_candidato),
#             msg='O texto do nome do canditado esta errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h4[data-info="seuPerfilTelefone"').text,
#             'Seu telefone: {}'.format(self.perfil_ehele.telefone_candidato),
#             msg='O texto do telefone do canditado esta errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h4[data-info="seuPerfilSalario"').text,
#             'Sua pretensão salarial: {}'.format(FaixaSalario(self.perfil_ehele.faixa_salario).label),
#             msg='O texto da pretensão salarial do canditado esta errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h4[data-info="seuPerfilEscolaridade"').text,
#             'Seu nivel de escolaridade: {}'.format(NivelEscolaridade(self.perfil_ehele.nivel_escolaridade).label),
#             msg='O texto do nivel de escolaridade do canditado esta errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h4[data-info="seuPerfilExperiencia"').text,
#             'Suas experiencias:\n{}'.format(self.perfil_ehele.experiencia),
#             msg='O texto das experiencias do canditado esta errado.'
#         )

#         #TODO continuar tem q ir para algum lugar, no caso edição de perfil
#         print('ARRUMAR AQUI')
        
#     ## FIM test_visualizar_perfil_candidato

#     def test_falhando_visualizar_perfil_candidato(self):
#         ''' 
#         Teste para vaizualizar o perfil do candidato, porem sem perfil e deve ser redirecionado para a tela de criar perfil.
#         '''
#         # Para logar o selenium na pagina. 
#         self.c.login(email=self.user_sem_perfil.email, password='VOU pegar teus d4d0s')
#         cookie = self.c.cookies['sessionid']
#         self.browser.get(self.live_server_url + '/candidato/visualizandoperfil')
#         self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
#         self.browser.refresh()
#         self.browser.get(self.live_server_url + '/candidato/visualizandoperfil')
        
#         # Entra na pagina de vizualizar perfil, porem por não ter perfil é redirecionado criar o perfil do candidato     
#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/criandoperfil', 
#             msg='Foi encontrada outra pagina, e não a url /candidato/criandoperfil.'
#         )

#     ## FIM test_falhando_visualizar_perfil_candidato

#     def test_empresa_acessando_visualizando_perfil(self):
#         ''' 
#         Teste de usuario empresa entra na pagina errada visualizando perfil, deve ser redirecinonada
#         '''
#         # Para logar o selenium na pagina. 
#         self.c.login(email=self.empresa_com_info.email, password='CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:')
#         cookie = self.c.cookies['sessionid']
#         self.browser.get(self.live_server_url + '/candidato/visualizandoperfil')
#         self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
#         self.browser.refresh()
#         self.browser.get(self.live_server_url + '/candidato/visualizandoperfil')
        
#         # Entra na pagina de criar o visualizar perfil do candidato    
#         # É redirecionado para o login   
#         self.assertNotEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/visualizandoperfil', 
#             msg='O usuario empresa não está sendo redirecionado na url /candidato/visualizandoperfil.'
#         )

#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/', 
#             msg='O usuario empresa deveria ser redirecionado para a url /, vindo de /candidato/visualizandoperfil.'
#         )

#         # Ao ser redirecionado, a pessoa confere o titulo da pagina para ver onde está.
#         self.assertEqual(
#             self.browser.title ,
#             'Django Vagas',
#             msg='O titulo da pagina não condiz com "Django Vagas".'
#         )

#     ## FIM test_empresa_acessando_visualizando_perfil