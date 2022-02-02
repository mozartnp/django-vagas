# import time

# from django.test import LiveServerTestCase, Client
# from selenium import webdriver

# class UsuarioTestCase(LiveServerTestCase):

#     #Para setar o navegador
#     def setUp(self): 
#         self.browser = webdriver.Firefox(executable_path='./geckodriver')

#     #Para fechar o navegador
#     def tearDown(self):
#         self.browser.quit()

#     # Testes funcionais do usuario
#     def test_pagina_boas_vindas_registro(self):
#         ''' 
#         Teste da pagina inicial. Onde o usuario vai para o registro.
#         '''
#         # instanciar o client
#         c = Client()

#         # A pessoa abre o site do Django Vagas
#         resposta = c.post('')
#         self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

#         self.browser.get(self.live_server_url + '')

#         # Ela confere o titulo da pagina para ver se está no site certo
#         self.assertEqual(
#             self.browser.title ,
#             'Django Vagas',
#             msg='O titulo da pagina não condiz com "Django Vagas".'
#         )

#         # A pessoa vê o anuncio e lê.
#         anuncio = self.browser.find_element_by_css_selector('section[data-info="boasVindasAnuncio"')
#         self.assertEqual(
#             anuncio.text,
#             'Django Vagas, a maior plataforma de empregos django do Brasil.\n\nSe você está procurando empregos, não perca tempo se cadastre.\nCaso seja uma empresa, cadastre-se e desfrute da nossa base de candidatos.',
#             msg='O anuncio está diferente do definido.'
#         )

#         # Fica interresada e vai se cadastrar. Para isso procura a navbar.
#         self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')

#         #Apos isso o botão de cadastro
#         cadastro = self.browser.find_element_by_css_selector('div[data-info="botaoCadastro"')
#         self.assertEqual(
#             cadastro.text,
#             'Cadastro',
#             msg='O texto do botão de cadastro está errado.'
#         )

#         #A pessoa clica no botão de cadastro.
#         cadastro.click()
#         self.assertEqual(self.browser.current_url, self.live_server_url + '/cadastro', msg='A pagina de cadastro não foi alcançada pelo botão de cadastro.')

#     def test_pagina_boas_vindas_login(self):
#         '''
#         Teste da pagina inicial. Onde o usuario vai para o login.
#         '''
#         self.browser.get(self.live_server_url + '')
 
#         # Ela confere o titulo da pagina para ver se está no site certo
#         self.assertEqual(
#             self.browser.title ,
#             'Django Vagas',
#             msg='O titulo da pagina não condiz com "Django Vagas".'
#         )

#          # Fica interresada e vai se cadastrar.
#         cadastro = self.browser.find_element_by_css_selector('div[data-info="botaoLogin"')
#         self.assertEqual(
#             cadastro.text,
#             'Login',
#             msg='O texto do botão de Login está errado.'
#         )

#         #A pessoa clica no botão de cadastro. 
#         cadastro.click()
#         self.assertEqual(self.browser.current_url, 
#             self.live_server_url + '/login', 
#             msg='A pagina de login não foi alcançada pelo botão de login.'
#         )

#     def test_cadastro_user(self):
#         '''
#         Teste para cadastro de um novo usuario. Sendo candidato.
#         '''
#         # instanciar o client
#         c = Client()

#         self.browser.get(self.live_server_url + '/cadastro')

#          # A pessoa abre a pagina de cadastro do Django Vagas
#         resposta = c.post('/cadastro')

#         self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

#         # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
#         self.assertEqual(
#             self.browser.title ,
#             'Cadastro',
#             msg='O titulo da pagina não condiz com "Cadastro".'
#         )
#         # Vê a navabar.
#         self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')
        
#         # A pessoa vê o anuncio e lê.
#         anuncio = self.browser.find_element_by_css_selector('section[data-info="cadastroUserAnuncio"')
#         self.assertEqual(
#             anuncio.text,
#             'Cadastre-se na nossa plataforma de empregos.\nA maior plataforma de empregos em Django do Brasil.',
#             msg='O anuncio está diferente do definido.'
#         )

#         # Procura o formulario de cadastro
#         self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="cadastroUserForm"'))

#         # Dentro do formulario procura os campos, email, senha e tipo de usuario
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
#             'Email',
#             msg='O texto de indicação do campo e-mail está errado.'
#         )
#         email = self.browser.find_element_by_css_selector('input[id="id_email"')
#         self.assertEqual(
#             email.get_attribute('placeholder'),
#             'Digite seu e-mail.',
#             msg='O texto do placeholder do e-mail está errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_tipo_user"').text,
#             'Tipo de cadastro\n---------\nEmpresa\nCandidato',
#             msg='O texto de indicação do campo seletor do cadastro está errado.'
#         )
#         tipo_user = self.browser.find_element_by_css_selector('select[id="id_tipo_user"')

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_password1"').text,
#             'Senha',
#             msg='O texto de indicação do campo password1 está errado.'
#         )
#         password1 = self.browser.find_element_by_css_selector('input[id="id_password1"')
#         self.assertEqual(
#             password1.get_attribute('placeholder'),
#             'Sua senha deve conter A-Z a-z 0-9',
#             msg='O texto do placeholder do password1 está errado.'
#         )

#         self.assertEqual(
#             self.browser.find_element_by_css_selector('div[data-info="campo_password2"').text,
#             'Confirmação de senha',
#             msg='O texto de indicação do campo password2 está errado.'
#         )
#         password2 = self.browser.find_element_by_css_selector('input[id="id_password2"')
#         self.assertEqual(
#             password2.get_attribute('placeholder'),
#             'Repita sua senha.',
#             msg='O texto do placeholder do password2 está errado.'
#         )

#         # Então a pessoa começa a preencher o cadastro
#         email.send_keys('gandalf@cizento.com')
#         tipo_user = self.browser.find_element_by_css_selector('option[value="CAND"')
#         tipo_user.click()
#         password1.send_keys('Minas Tirith 7 aneis')
#         password2.send_keys('Minas Tirith 7 aneis')
         
#         # Procura o botão para concluir o cadastro e clica nele
#         botaoCadastrando = self.browser.find_element_by_css_selector('div[data-info="botaoCadastrando"')
#         botaoCadastrando.click()

#         # E espera ir para uma proxima pagina, já logado. Como ele se cadastrou como candidato, vai para a pagina de criar o perfil do candidato
#         time.sleep(1)
#         self.assertEqual(
#             self.browser.current_url,
#             self.live_server_url + '/candidato/criandoperfil', 
#             msg='A pagina de criar perfil do candidato não foi alcançada apos cadastro.'
#         )