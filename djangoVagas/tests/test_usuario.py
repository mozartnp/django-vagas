import time

from selenium import webdriver

from django.test import LiveServerTestCase, Client
from django.contrib.auth import hashers

from user.models import User

from candidato.models.perfil_models import PerfilModel

from empresa.models.info_model import InfoModel

class UsuarioTestCase(LiveServerTestCase):

    #Para setar o navegador
    def setUp(self): 
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        
        self.empresa_sem_info = User.objects.create(
            email= "hackeasdr@russo.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_sem_info.password = hashers.make_password(self.empresa_sem_info.password)
        self.empresa_sem_info.save()

        ## FIM empresa_sem_info

        self.empresa_com_info = User.objects.create(
            email= "empresaaaario666@serio.com",
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

        self.candidato_sem_perfil = User.objects.create(
            email= "hackdaer@russo.com",
            password= "VOU pegar teus d4d0s",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.candidato_sem_perfil.password = hashers.make_password(self.candidato_sem_perfil.password)
        self.candidato_sem_perfil.save()

        ## FIM candidato_sem_perfil

        self.candidato_com_perfil = User.objects.create(
            email= "eheale@bol.com",
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

    # FIM tearDown

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

        # Fica interresada e vai se cadastrar. Para isso procura a navbar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')

        #Apos isso o botão de cadastro
        cadastro = self.browser.find_element_by_css_selector('div[data-info="botaoCadastro"')
        self.assertEqual(
            cadastro.text,
            'Cadastro',
            msg='O texto do botão de cadastro está errado.'
        )

        #A pessoa clica no botão de cadastro.
        cadastro.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + '/cadastro', msg='A pagina de cadastro não foi alcançada pelo botão de cadastro.')

    ## FIM test_pagina_boas_vindas_registro

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

         # A pessoas deseja logar no sistema.
        cadastro = self.browser.find_element_by_css_selector('div[data-info="botaoLogin"')
        self.assertEqual(
            cadastro.text,
            'Login',
            msg='O texto do botão de Login está errado.'
        )

        #A pessoa clica no botão de login. 
        cadastro.click()
        self.assertEqual(self.browser.current_url, 
            self.live_server_url + '/login', 
            msg='A pagina de login não foi alcançada pelo botão de login.'
        )

    ## FIM test_pagina_boas_vindas_login

    def test_cadastro_user_candidato(self):
        '''
        Teste para cadastro de um novo usuario. Sendo candidato.
        '''
        # instanciar o client
        c = Client()

        self.browser.get(self.live_server_url + '/cadastro')

         # A pessoa abre a pagina de cadastro do Django Vagas
        resposta = c.post('/cadastro')

        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Cadastro',
            msg='O titulo da pagina não condiz com "Cadastro".'
        )
        # Vê a navabar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')
        
        # A pessoa vê o anuncio e lê.
        anuncio = self.browser.find_element_by_css_selector('section[data-info="cadastroUserAnuncio"')
        self.assertEqual(
            anuncio.text,
            'Cadastre-se na nossa plataforma de empregos.\nA maior plataforma de empregos em Django do Brasil.',
            msg='O anuncio está diferente do definido.'
        )

        # Procura o formulario de cadastro
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="cadastroUserForm"'))

        # Dentro do formulario procura os campos, email, senha e tipo de usuario
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
            'Email',
            msg='O texto de indicação do campo e-mail está errado.'
        )
        email = self.browser.find_element_by_css_selector('input[id="id_email"')
        self.assertEqual(
            email.get_attribute('placeholder'),
            'Digite seu e-mail.',
            msg='O texto do placeholder do e-mail está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_tipo_user"').text,
            'Tipo de cadastro\n---------\nEmpresa\nCandidato',
            msg='O texto de indicação do campo seletor do cadastro está errado.'
        )
        tipo_user = self.browser.find_element_by_css_selector('select[id="id_tipo_user"')

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password1"').text,
            'Senha',
            msg='O texto de indicação do campo password1 está errado.'
        )
        password1 = self.browser.find_element_by_css_selector('input[id="id_password1"')
        self.assertEqual(
            password1.get_attribute('placeholder'),
            'Sua senha deve conter A-Z a-z 0-9',
            msg='O texto do placeholder do password1 está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password2"').text,
            'Confirmação de senha',
            msg='O texto de indicação do campo password2 está errado.'
        )
        password2 = self.browser.find_element_by_css_selector('input[id="id_password2"')
        self.assertEqual(
            password2.get_attribute('placeholder'),
            'Repita sua senha.',
            msg='O texto do placeholder do password2 está errado.'
        )

        # Então a pessoa começa a preencher o cadastro
        email.send_keys('gandalf@cizento.com')
        tipo_user = self.browser.find_element_by_css_selector('option[value="CAND"')
        tipo_user.click()
        password1.send_keys('Minas Tirith 7 aneis')
        password2.send_keys('Minas Tirith 7 aneis')
         
        # Procura o botão para concluir o cadastro e clica nele
        botaoCadastrando = self.browser.find_element_by_css_selector('div[data-info="botaoCadastrando"')
        botaoCadastrando.click()

        # E espera ir para uma proxima pagina, já logado. Como ele se cadastrou como candidato, vai para a pagina de criar o perfil do candidato
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/candidato/criandoperfil', 
            msg='A pagina de criar perfil do candidato não foi alcançada apos cadastro.'
        )

    ## FIM test_cadastro_user_candidato

    def test_cadastro_user_empresa(self):
        '''
        Teste para cadastro de um novo usuario. Sendo empresa.
        '''
        # instanciar o client
        c = Client()

        self.browser.get(self.live_server_url + '/cadastro')

         # A pessoa abre a pagina de cadastro do Django Vagas
        resposta = c.post('/cadastro')

        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está no site certo
        self.assertEqual(
            self.browser.title ,
            'Cadastro',
            msg='O titulo da pagina não condiz com "Cadastro".'
        )
        # Vê a navabar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')
        
        # A pessoa vê o anuncio e lê.
        anuncio = self.browser.find_element_by_css_selector('section[data-info="cadastroUserAnuncio"')
        self.assertEqual(
            anuncio.text,
            'Cadastre-se na nossa plataforma de empregos.\nA maior plataforma de empregos em Django do Brasil.',
            msg='O anuncio está diferente do definido.'
        )

        # Procura o formulario de cadastro
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="cadastroUserForm"'))

        # Dentro do formulario procura os campos, email, senha e tipo de usuario
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
            'Email',
            msg='O texto de indicação do campo e-mail está errado.'
        )
        email = self.browser.find_element_by_css_selector('input[id="id_email"')
        self.assertEqual(
            email.get_attribute('placeholder'),
            'Digite seu e-mail.',
            msg='O texto do placeholder do e-mail está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_tipo_user"').text,
            'Tipo de cadastro\n---------\nEmpresa\nCandidato',
            msg='O texto de indicação do campo seletor do cadastro está errado.'
        )
        tipo_user = self.browser.find_element_by_css_selector('select[id="id_tipo_user"')

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password1"').text,
            'Senha',
            msg='O texto de indicação do campo password1 está errado.'
        )
        password1 = self.browser.find_element_by_css_selector('input[id="id_password1"')
        self.assertEqual(
            password1.get_attribute('placeholder'),
            'Sua senha deve conter A-Z a-z 0-9',
            msg='O texto do placeholder do password1 está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password2"').text,
            'Confirmação de senha',
            msg='O texto de indicação do campo password2 está errado.'
        )
        password2 = self.browser.find_element_by_css_selector('input[id="id_password2"')
        self.assertEqual(
            password2.get_attribute('placeholder'),
            'Repita sua senha.',
            msg='O texto do placeholder do password2 está errado.'
        )

        # Então a pessoa começa a preencher o cadastro para empresa
        email.send_keys('bruxao@thea.com')
        tipo_user = self.browser.find_element_by_css_selector('option[value="EMPR"')
        tipo_user.click()
        password1.send_keys('Minas Tirith 7 aneis')
        password2.send_keys('Minas Tirith 7 aneis')
         
        # Procura o botão para concluir o cadastro e clica nele
        botaoCadastrando = self.browser.find_element_by_css_selector('div[data-info="botaoCadastrando"')
        botaoCadastrando.click()

        # E espera ir para uma proxima pagina, já logado. Como ele se cadastrou como candidato, vai para a pagina de criar o perfil do candidato
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='A pagina de cadastrar informações da empresa não foi alcançada apos cadastro.'
        )
        
    ## FIM test_cadastro_user_empresa

    def test_login_user_candidato_sem_perfil(self):
        '''
        Teste para login usuario candidato, sem perfil. Deve ir para a pagina criandoperfil.
        '''
        # instanciar o client
        c = Client()

        self.browser.get(self.live_server_url + '/login')

         # A pessoa abre a pagina de login do Django Vagas
        resposta = c.post('/login')

        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está na pagina certa
        self.assertEqual(
            self.browser.title ,
            'Login',
            msg='O titulo da pagina não condiz com "Login".'
        )
        # Vê a navabar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')

        # Procura o formulario de login
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="loginForm"'))

        # A pessoa lê.
        self.assertEqual(
            self.browser.find_element_by_css_selector('h3[data-info="textoLogin"').text,
            'Login',
            msg='O texto do login está diferente do definido.'
        )

        # Dentro do formulario procura os campos, email e senha 
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
            'Email',
            msg='O texto de indicação do campo e-mail está errado.'
        )
        email = self.browser.find_element_by_css_selector('input[id="id_email"')
        self.assertEqual(
            email.get_attribute('placeholder'),
            'Digite seu e-mail',
            msg='O texto do placeholder do e-mail está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password"').text,
            'Senha',
            msg='O texto de indicação do campo password1 está errado.'
        )
        password = self.browser.find_element_by_css_selector('input[id="id_password"')
        self.assertEqual(
            password.get_attribute('placeholder'),
            'Digite sua senha',
            msg='O texto do placeholder do password está errado.'
        )

        # Então a pessoa começa a colocar as informações
        email.send_keys("hackdaer@russo.com")
        password.send_keys("VOU pegar teus d4d0s")

         
        # Procura o botão para concluir o login e clica nele
        botaoLogin = self.browser.find_element_by_css_selector('button[data-info="botaoLogin"')
        self.assertEqual(
            botaoLogin.text,
            'Logar',
            msg='O texto do botão está errado.'
        )
        botaoLogin.click()

        # E espera ir para uma proxima pagina, já logado, Criar o perfil do candidato
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/candidato/criandoperfil', 
            msg='A pagina de criar perfil do candidato não foi alcançada apos login.'
        )

    ## FIM test_login_user_candidato_sem_perfil

    def test_login_user_candidato_com_perfil(self):
        '''
        Teste para login usuario candidato, com perfil. Deve ir para a pagina visualizandoperfil.
        '''
        # instanciar o client
        c = Client()

        self.browser.get(self.live_server_url + '/login')

         # A pessoa abre a pagina de login do Django Vagas
        resposta = c.post('/login')

        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está na pagina certa
        self.assertEqual(
            self.browser.title ,
            'Login',
            msg='O titulo da pagina não condiz com "Login".'
        )
        # Vê a navabar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')

        # Procura o formulario de login
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="loginForm"'))

        # A pessoa lê.
        self.assertEqual(
            self.browser.find_element_by_css_selector('h3[data-info="textoLogin"').text,
            'Login',
            msg='O texto do login está diferente do definido.'
        )

        # Dentro do formulario procura os campos, email e senha 
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
            'Email',
            msg='O texto de indicação do campo e-mail está errado.'
        )
        email = self.browser.find_element_by_css_selector('input[id="id_email"')
        self.assertEqual(
            email.get_attribute('placeholder'),
            'Digite seu e-mail',
            msg='O texto do placeholder do e-mail está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password"').text,
            'Senha',
            msg='O texto de indicação do campo password1 está errado.'
        )
        password = self.browser.find_element_by_css_selector('input[id="id_password"')
        self.assertEqual(
            password.get_attribute('placeholder'),
            'Digite sua senha',
            msg='O texto do placeholder do password está errado.'
        )

        # Então a pessoa começa a colocar as informações
        email.send_keys("eheale@bol.com")
        password.send_keys("CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")

         
        # Procura o botão para concluir o login e clica nele
        botaoLogin = self.browser.find_element_by_css_selector('button[data-info="botaoLogin"')
        self.assertEqual(
            botaoLogin.text,
            'Logar',
            msg='O texto do botão está errado.'
        )
        botaoLogin.click()

        # E espera ir para uma proxima pagina, já logado, Visualizar o perfil do candidato
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/candidato/visualizandoperfil', 
            msg='A pagina de visualizar perfil do candidato não foi alcançada apos login.'
        )

    ## FIM test_login_user_candidato_com_perfil

    def test_login_user_empresa_sem_info(self):
        '''
        Teste para login usuario empresa, sem perfil. Deve ir para a pagina cadastrandoinfo.
        '''
        # instanciar o client
        c = Client()

        self.browser.get(self.live_server_url + '/login')

         # A pessoa abre a pagina de login do Django Vagas
        resposta = c.post('/login')

        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está na pagina certa
        self.assertEqual(
            self.browser.title ,
            'Login',
            msg='O titulo da pagina não condiz com "Login".'
        )
        # Vê a navabar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')

        # Procura o formulario de login
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="loginForm"'))

        # A pessoa lê.
        self.assertEqual(
            self.browser.find_element_by_css_selector('h3[data-info="textoLogin"').text,
            'Login',
            msg='O texto do login está diferente do definido.'
        )

        # Dentro do formulario procura os campos, email e senha 
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
            'Email',
            msg='O texto de indicação do campo e-mail está errado.'
        )
        email = self.browser.find_element_by_css_selector('input[id="id_email"')
        self.assertEqual(
            email.get_attribute('placeholder'),
            'Digite seu e-mail',
            msg='O texto do placeholder do e-mail está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password"').text,
            'Senha',
            msg='O texto de indicação do campo password1 está errado.'
        )
        password = self.browser.find_element_by_css_selector('input[id="id_password"')
        self.assertEqual(
            password.get_attribute('placeholder'),
            'Digite sua senha',
            msg='O texto do placeholder do password está errado.'
        )

        # Então a pessoa começa a colocar as informações
        email.send_keys("hackeasdr@russo.com")
        password.send_keys("CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")

         
        # Procura o botão para concluir o login e clica nele
        botaoLogin = self.browser.find_element_by_css_selector('button[data-info="botaoLogin"')
        self.assertEqual(
            botaoLogin.text,
            'Logar',
            msg='O texto do botão está errado.'
        )
        botaoLogin.click()

        # E espera ir para uma proxima pagina, já logado, Visualizar o perfil do candidato
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/cadastrandoinfo', 
            msg='A pagina de cadastrar info da empresa não foi alcançada apos login.'
        )

    ## FIM test_login_user_empresa_sem_info

    def test_login_user_empresa_com_info(self):
        '''
        Teste para login usuario empresa, com info. Deve ir para a pagina visualizandoinfo.
        '''
        # instanciar o client
        c = Client()

        self.browser.get(self.live_server_url + '/login')

         # A pessoa abre a pagina de login do Django Vagas
        resposta = c.post('/login')

        self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

        # Ao entrar na pagina a pessoa confere o titulo da pagina para ver se está na pagina certa
        self.assertEqual(
            self.browser.title ,
            'Login',
            msg='O titulo da pagina não condiz com "Login".'
        )
        # Vê a navabar.
        self.browser.find_element_by_css_selector('section[data-info="navbar-login-cadastro"')

        # Procura o formulario de login
        self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="loginForm"'))

        # A pessoa lê.
        self.assertEqual(
            self.browser.find_element_by_css_selector('h3[data-info="textoLogin"').text,
            'Login',
            msg='O texto do login está diferente do definido.'
        )

        # Dentro do formulario procura os campos, email e senha 
        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_email"').text,
            'Email',
            msg='O texto de indicação do campo e-mail está errado.'
        )
        email = self.browser.find_element_by_css_selector('input[id="id_email"')
        self.assertEqual(
            email.get_attribute('placeholder'),
            'Digite seu e-mail',
            msg='O texto do placeholder do e-mail está errado.'
        )

        self.assertEqual(
            self.browser.find_element_by_css_selector('div[data-info="campo_password"').text,
            'Senha',
            msg='O texto de indicação do campo password1 está errado.'
        )
        password = self.browser.find_element_by_css_selector('input[id="id_password"')
        self.assertEqual(
            password.get_attribute('placeholder'),
            'Digite sua senha',
            msg='O texto do placeholder do password está errado.'
        )

        # Então a pessoa começa a colocar as informações
        email.send_keys("empresaaaario666@serio.com")
        password.send_keys("CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")

         
        # Procura o botão para concluir o login e clica nele
        botaoLogin = self.browser.find_element_by_css_selector('button[data-info="botaoLogin"')
        self.assertEqual(
            botaoLogin.text,
            'Logar',
            msg='O texto do botão está errado.'
        )
        botaoLogin.click()

        # E espera ir para uma proxima pagina, já logado, Visualizar o info da empresa
        time.sleep(1)
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/empresa/visualizandoinfo', 
            msg='A pagina de visualizar info da empresa não foi alcançada apos login.'
        )

    ## FIM test_login_user_empresa_com_info