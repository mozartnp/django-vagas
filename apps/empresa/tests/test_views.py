from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import hashers

from empresa.models.info_model import InfoModel

from candidato.models.perfil_models import PerfilModel

from user.models import User

class TestInfoViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.empresa_sem_info = User.objects.create(
            email= "testasde@testando.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_sem_info.password = hashers.make_password(self.empresa_sem_info.password)
        self.empresa_sem_info.save()

        ## FIM empresa_sem_info

        self.empresa_com_info = User.objects.create(
            email= "sonoaa@damulesta.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_com_info.password = hashers.make_password(self.empresa_com_info.password)
        self.empresa_com_info.save()

        InfoModel.objects.create(
            nome_empresa = "Longe",
            telefone_empresa = "(81) 9.9999-9999",
            contato_empresa = "Marcelinho",
            user_id = self.empresa_com_info.id
        )

        ## FIM empresa_com_info

        self.candidao_errado = User.objects.create(
            email= "lugar@errado.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.candidao_errado.password = hashers.make_password(self.candidao_errado.password)
        self.candidao_errado.save()

        PerfilModel.objects.create(
            nome_candidato= "Teste testador",
            telefone_candidato= "(81) 1.5555-8765",
            faixa_salario= "<2k_3k>",
            nivel_escolaridade= "pos",
            experiencia= "Planador",
            user_id= self.candidao_errado.id,
        )

        ## FIM candidao_errado


    ## FIM setUp
        
    def test_cadastrandoinfo_view (self):
        '''
        Teste da view do cadastrando info
        '''
        # While para testar tanto logado quanto não logado
        validador = 3
        logado = False
        empresa = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('cadastrandoinfo'), follow=True)
                response = self.c.get(reverse('cadastrandoinfo'))
        
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de cadastrando info.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de cadastrando info não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view cadastrando info está errado, deveria ser 302, apos ser redirecionado.'
                )
        
            elif logado:
                if not empresa:
                    # Para preparar o client com login
                    self.c.login(email=self.candidao_errado.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('cadastrandoinfo'), follow=True)
                    empresa = True
     
                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/',
                        msg= 'O usuario logado mas é um candidato, deveria ir para pagina de boas vindas, algo aconteceu aqui, vindo de cadastrando info.'
                    )
                
                    # Para verificar se esta sendo redirecionada corretamente
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code do boas vindas apos redirecinamento de cadastrando info não é 200'
                    )
            
                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response.status_code,
                        302,
                        msg='O status code da view cadastrando info está errado, deveria ser 302, apos ser redirecionado.'
                    )

                elif empresa:
                    # Para preparar o client com login
                    self.c.login(email=self.empresa_sem_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('cadastrandoinfo'), follow=True)

                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/empresa/cadastrandoinfo',
                        msg= 'A url da view cadastrando info logado, está com erro.'
                    )

                    # Para verificar se as templates que a view usa está certo 
                        #base.html
                    self.assertTemplateUsed(
                        response_seguindo,
                        'base.html',
                        msg_prefix= 'A template base.html na view cadastrando info está com erro.'
                    )

                        # empresa/cadastrandoinfo.html
                    self.assertTemplateUsed(
                        response_seguindo,
                        'empresa/cadastrandoinfo.html',
                        msg_prefix= 'A template empresa/cadastrandoinfo.html na view cadastrando info está com erro.'
                    )

                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code da view criando perfil logado, está errado, deveria ser 200.'
                    )
            
            logado = True
            validador -= 1

    ## FIM test_cadastrandoinfo_view
    
    def test_inseridoinfo_view(self): #TODO
        '''
        Teste da view do inserindo info
        '''
        pass

    ## FIM test_inseridoinfo_view

    def test_visualizainfo_view(self):
        '''
        Teste da view do visualizando info
        '''
        # While para testar tanto logado quanto não logado, quanto com ou sem info
        validador = 4
        logado = False
        info = False
        empresa = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('visualizandoinfo'), follow=True)
                response = self.c.get(reverse('visualizandoinfo'))
                logado = True
                
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de visualizando ino.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de visualizando info não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view visualizando info não é 302'
                )
            
            elif logado:
                #IF para validar o tipo de usuario
                if not empresa:
                    # Para preparar o client com login
                    self.c.login(email=self.candidao_errado.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('visualizandoinfo'), follow=True)
                    response = self.c.get(reverse('visualizandoinfo'))
                    empresa = True
                            
                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/',
                        msg= "Empresa sem info deveria ir para pagina de cadastrando info, algo aconteceu aqui, vindo de visualizando info."
                    )
                
                    # Para verificar se esta sendo redirecionada corretamente
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code de cadastrando info apos redirecinamento de visualizando info não é 200'
                    )
            
                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response.status_code,
                        302,
                        msg='O status code da view visualizando info não é 302'
                    )

                elif empresa:
                    #If para validar o redirecionamento da view caso a empresa não tenha info
                    if not info:
                        # Para preparar o client com login
                        self.c.login(email=self.empresa_sem_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('visualizandoinfo'), follow=True)
                        response = self.c.get(reverse('visualizandoinfo'))
                        info = True
                            
                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/empresa/cadastrandoinfo',
                            msg= 'Empresa sem info, deveria ir para pagina de casdranto info, algo aconteceu aqui, vindo de visualizando info.'
                        )
                    
                        # Para verificar se esta sendo redirecionada corretamente
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code de cadastrando info apos redirecinamento de visualizando info não é 200'
                        )
                
                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response.status_code,
                            302,
                            msg='O status code da view visualizando info não é 302'
                        )

                    elif info:
                        # Para preparar o client com login
                        self.c.login(email=self.empresa_com_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('visualizandoinfo'), follow=True)

                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/empresa/visualizandoinfo',
                            msg= 'A url da view visualizando info logado e com info, está com erro.'
                        )

                        # Para verificar se as templates que a view usa está certo 
                            #base.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'base.html',
                            msg_prefix= 'A template base.html na view visualizando info está com erro.'
                        )

                            #partials/_sidebar.html.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'partials/_sidebar.html',
                            msg_prefix= 'A template _sidebar.html na view visualizando info está com erro.'
                        )

                            # visualizandoinfo.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'empresa/visualizandoinfo.html',
                            msg_prefix= 'A template visualizandoinfo.html na view visualizando info está com erro.'
                        )

                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code da view visualizando info logado e com info, está errado'
                        )
                              
            validador -= 1
            
    ## FIM test_visualizainfo_view

    def test_criandovaga_view(self):
        '''
        Teste da view do criando vaga
        '''
        # While para testar tanto logado quanto não logado, quanto com ou sem info
        validador = 4
        logado = False
        info = False
        empresa = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('criandovaga'), follow=True)
                response = self.c.get(reverse('criandovaga'))
                logado = True
                
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de criando vaga.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de criando vaga não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view criando vaga não é 302'
                )
            
            elif logado:
                #IF para validar o tipo de usuario
                if not empresa:
                    # Para preparar o client com login
                    self.c.login(email=self.candidao_errado.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('criandovaga'), follow=True)
                    response = self.c.get(reverse('criandovaga'))
                    empresa = True
                            
                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/',
                        msg= "Empresa sem info deveria ir para pagina de cadastrando info, algo aconteceu aqui, vindo de criando vaga."
                    )
                
                    # Para verificar se esta sendo redirecionada corretamente
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code de cadastrando info apos redirecinamento de criando vaga não é 200'
                    )
            
                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response.status_code,
                        302,
                        msg='O status code da view criando vaga não é 302'
                    )

                elif empresa:
                    #If para validar o redirecionamento da view caso a empresa não tenha info
                    if not info:
                        # Para preparar o client com login
                        self.c.login(email=self.empresa_sem_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('criandovaga'), follow=True)
                        response = self.c.get(reverse('criandovaga'))
                        info = True
                                                    
                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/empresa/cadastrandoinfo',
                            msg= 'Empresa sem info, deveria ir para pagina de casdranto info, algo aconteceu aqui, vindo de criando vaga.'
                        )
                    
                        # Para verificar se esta sendo redirecionada corretamente
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code de cadastrando info apos redirecinamento de criando vaga não é 200'
                        )
                
                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response.status_code,
                            302,
                            msg='O status code da view criando vaga não é 302'
                        )

                    elif info:
                        # Para preparar o client com login
                        self.c.login(email=self.empresa_com_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('criandovaga'), follow=True)

                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/empresa/criandovaga',
                            msg= 'A url da view criando vaga logado e com info, está com erro.'
                        )

                        # Para verificar se as templates que a view usa está certo 
                            #base.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'base.html',
                            msg_prefix= 'A template base.html na view criando vaga está com erro.'
                        )

                            #partials/_sidebar.html.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'partials/_sidebar.html',
                            msg_prefix= 'A template _sidebar.html na view criando vaga está com erro.'
                        )

                            # criandovaga.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'empresa/criandovaga.html',
                            msg_prefix= 'A template criandovaga.html na view criando vaga está com erro.'
                        )

                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code da view criando vaga logado e com info, está errado'
                        )
                              
            validador -= 1
   
   ## FIM test_criandovaga_view

    def test_inserindovaga_view(self): #TODO
        '''
        Teste da view do inserindo vaga
        '''
        pass
   
   ## FIM test_inserindovaga_view

    def test_visualizandosuasvagas_view(self):
        '''
        Teste da view do visualizando suas vagas
        '''
        # While para testar tanto logado quanto não logado, quanto com ou sem info
        validador = 4
        logado = False
        info = False
        empresa = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('visualizandosuasvagas'), follow=True)
                response = self.c.get(reverse('visualizandosuasvagas'))
                logado = True
                
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de visualizando suas vagas.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de visualizando suas vagas não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view visualizando suas vagas não é 302'
                )
            
            elif logado:
                #IF para validar o tipo de usuario
                if not empresa:
                    # Para preparar o client com login
                    self.c.login(email=self.candidao_errado.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('visualizandosuasvagas'), follow=True)
                    response = self.c.get(reverse('visualizandosuasvagas'))
                    empresa = True
                            
                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/',
                        msg= "Empresa sem info deveria ir para pagina de boas vindas, algo aconteceu aqui, vindo de visualizando suas vagas."
                    )
                
                    # Para verificar se esta sendo redirecionada corretamente
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code de boas vindas apos redirecinamento de visualizando suas vagas não é 200'
                    )
            
                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response.status_code,
                        302,
                        msg='O status code da view visualizando suas vagas não é 302'
                    )

                elif empresa:
                    #If para validar o redirecionamento da view caso a empresa não tenha info
                    if not info:
                        # Para preparar o client com login
                        self.c.login(email=self.empresa_sem_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('visualizandosuasvagas'), follow=True)
                        response = self.c.get(reverse('visualizandosuasvagas'))
                        info = True
                            
                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/empresa/cadastrandoinfo',
                            msg= 'Empresa sem info, deveria ir para pagina de casdranto info, algo aconteceu aqui, vindo de visualizando suas vagas.'
                        )
                    
                        # Para verificar se esta sendo redirecionada corretamente
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code de cadastrando info apos redirecinamento de visualizando suas vagas não é 200'
                        )
                
                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response.status_code,
                            302,
                            msg='O status code da view visualizando suas vagas não é 302'
                        )

                    elif info:
                        # Para preparar o client com login
                        self.c.login(email=self.empresa_com_info.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('visualizandosuasvagas'), follow=True)

                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/empresa/visualizandosuasvagas',
                            msg= 'A url da view visualizando suas vagas logado e com info, está com erro.'
                        )

                        # Para verificar se as templates que a view usa está certo 
                            #base.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'base.html',
                            msg_prefix= 'A template base.html na view visualizando suas vagas está com erro.'
                        )

                            #partials/_sidebar.html.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'partials/_sidebar.html',
                            msg_prefix= 'A template _sidebar.html na view visualizando suas vagas está com erro.'
                        )

                            # visualizandosuasvagas.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'empresa/visualizandosuasvagas.html',
                            msg_prefix= 'A template visualizandosuasvagas.html na view visualizando suas vagas está com erro.'
                        )

                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code da view visualizando suas vagas logado e com info, está errado'
                        )
                              
            validador -= 1
           
   ## FIM test_visualizandosuasvagas_view