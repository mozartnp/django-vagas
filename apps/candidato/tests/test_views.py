from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import hashers

from candidato.views import perfil_views
from candidato.models.perfil_models import PerfilModel

from empresa.models.info_model import InfoModel

from user.models import User

class TestWebsiteViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.user_sem_perfil = User.objects.create(
            email= "teste@testando.com",
            password= "Apesar de voce, 4m4nh4",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.user_sem_perfil.password = hashers.make_password(self.user_sem_perfil.password)
        self.user_sem_perfil.save()

        ## FIM user_sem_perfil

        #Criando um novo usuario com perfil
        self.user_com_perfil = User.objects.create(
            email= "testando@teste.com",
            password= "Caramujo, e marujos 4m4nh4",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.user_com_perfil.password = hashers.make_password(self.user_com_perfil.password)
        self.user_com_perfil.save()

        PerfilModel.objects.create(
            nome_candidato= "Teste testador",
            telefone_candidato= "(81) 1.5555-8765",
            faixa_salario= "<2k_3k>",
            nivel_escolaridade= "pos",
            experiencia= "Planador",
            user_id= self.user_com_perfil.id,
        )

        ## FIM user_com_perfil

        self.empresa_errada = User.objects.create(
            email= "cachorro@damulesta.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_errada.password = hashers.make_password(self.empresa_errada.password)
        self.empresa_errada.save()

        self.info_empresa = InfoModel.objects.create(
            nome_empresa= "Criando sonhos",
            telefone_empresa= "(81) 1.1234-8765",
            contato_empresa= "Marcelinho",
            user_id= self.empresa_errada.id,
        )

        ## FIM empresa_errada

    ## FIM setUp
        
    def test_criandoperfil_view(self):
        '''
        Teste da view do criando perfil
        '''
        # While para testar tanto logado quanto não logado
        validador = 3
        logado = False
        candidato = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('criandoperfil'), follow=True)
                response = self.c.get(reverse('criandoperfil'))
        
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de criando perfil.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de criando perfil não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view criando perfil está errado, deveria ser 302, apos ser redirecionado.'
                )
        
            elif logado:
                if not candidato:
                    # Para preparar o client com login
                    self.c.login(email=self.empresa_errada.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('criandoperfil'), follow=True)
                    response = self.c.get(reverse('criandoperfil'))
                    candidato = True
     
                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/',
                        msg= 'O usuario logado mas é uma empresa, deveria ir para pagina de boas vindas, algo aconteceu aqui, vindo de criando pefil.'
                    )
                
                    # Para verificar se esta sendo redirecionada corretamente
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code de boas vindas apos redirecinamento de criando pefil não é 200'
                    )
            
                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response.status_code,
                        302,
                        msg='O status code da view criando pefil está errado, deveria ser 302, apos ser redirecionado.'
                    )

                elif candidato:
                    # Para preparar o client com login
                    self.c.login(email=self.user_sem_perfil.email, password='Apesar de voce, 4m4nh4' )
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('criandoperfil'), follow=True)

                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/candidato/criandoperfil',
                        msg= 'A url da view criando perfil logado, está com erro.'
                    )

                    # Para verificar se as templates que a view usa está certo 
                        #base.html
                    self.assertTemplateUsed(
                        response_seguindo,
                        'base.html',
                        msg_prefix= 'A template base.html na view criandoperfil está com erro.'
                    )

                        # criandoperfil.html
                    self.assertTemplateUsed(
                        response_seguindo,
                        'candidato/criandoperfil.html',
                        msg_prefix= 'A template criandoperfil.html na view criandoperfil está com erro.'
                    )

                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code da view criando perfil logado, está errado, deveria ser 200.'
                    )
                
            logado = True
            validador -= 1

    ## FIM test_criandoperfil_view

    def test_inseridoperfil_view(self): #TODO
        # While para testar tanto logado quanto não logado
        validador = 2
        logado = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('inseridoperfil'), follow=True)
                response = self.c.get(reverse('inseridoperfil'))
                            
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de inserindo perfil.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de inserindo perfil não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view inserindo perfil está errado, deveria ser 302, apos ser redirecionado.'
                )
        
            # elif logado:
            #     #TODO Arrumar aqui, não consigo passar o login neste teste/view...
            #     Para preparar o client com login
            #     self.c.login(email=self.user_sem_perfil.email, password='Apesar de voce, 4m4nh4')
            #     form_post = {
            #         'nome_candidato' : "Eh ele",
            #         'telefone_candidato' : "(81) 9.9999-9999",
            #         'faixa_salario' : "<1k_2k>",
            #         'nivel_escolaridade' : "doutorado",
            #         'experiencia' : "Tudo e um pouco mais.",
            #         'user_id' : self.user_sem_perfil.id,
            #     }
         
            #     #Para instaciar o client a pagina com login
            #     response_seguindo = self.c.get(reverse('inseridoperfil'), follow=True)
            #     response = self.c.get(reverse('inseridoperfil'))

            #     Para preparar o client com login
            #     self.c.login(email=self.user_sem_perfil.email, password='Apesar de voce, 4m4nh4')
            #     Para instaciar o client a pagina com login
            #     response_seguindo = self.c.get(reverse('inseridoperfil'), data=form_post, follow=True)
            #     response = self.c.get(reverse('inseridoperfil'), data=form_post)

            #     print()   
            #     print("###1 ", response.request)
            #     print("###2 ", response)
            #     print()
            #     print("###3 ", response_seguindo.request)
            #     print("###4 ", response_seguindo)
            #     print("###5 ", response_seguindo.redirect_chain)

            #     # Para ver se está na url certa
            #     self.assertEqual(
            #         response_seguindo.request['PATH_INFO'],
            #         '/candidato/criandoperfil',
            #         msg= 'A url da view criando perfil logado, está com erro.'
            #     )

            #     # Para verificar se esta sendo redirecionada corretamente
            #     self.assertEqual(
            #         response_seguindo.status_code,
            #         200,
            #         msg='O status code da nova view acessada apos redirecinamento de inserindo perfil não é 200.'
            #     )

            #     # Para verificar se view esta com o status code correto
            #     self.assertEqual(
            #         response.status_code,
            #         302,
            #         msg='O status code da view inserindo perfil está errado, deveria ser 302, apos ser redirecionado.'
            #     )
            
            logado = True
            validador -= 1
    
    ## FIM test_inseridoperfil_view

    def test_visualizandoperfil_view(self):
        '''
        Teste da view do visualizando perfil
        '''
        # While para testar tanto logado quanto não logado
        validador = 4
        logado = False
        perfil = False
        candidato = False
        while validador > 0 :
            if not logado:
                #Para instaciar o client a pagina sem logar
                response_seguindo = self.c.get(reverse('visualizandoperfil'), follow=True)
                response = self.c.get(reverse('visualizandoperfil'))
                
                # Para ver se está na url certa
                self.assertEqual(
                    response_seguindo.request['PATH_INFO'],
                    '/login',
                    msg= 'O usuario não logado, deveria ir para pagina de login, algo aconteceu aqui, vindo de visualizando perfil.'
                )
            
                # Para verificar se esta sendo redirecionada corretamente
                self.assertEqual(
                    response_seguindo.status_code,
                    200,
                    msg='O status code do login apos redirecinamento de visualizando perfil não é 200'
                )
        
                # Para verificar se view esta com o status code correto
                self.assertEqual(
                    response.status_code,
                    302,
                    msg='O status code da view visualizando perfil não é 302'
                )

            elif logado:
                #IF para validar o tipo de usuario
                if not candidato:
                    # Para preparar o client com login
                    self.c.login(email=self.empresa_errada.email, password="CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:")
                    #Para instaciar o client a pagina com login
                    response_seguindo = self.c.get(reverse('visualizandoperfil'), follow=True)
                    response = self.c.get(reverse('visualizandoperfil'))
                    candidato = True
     
                    # Para ver se está na url certa
                    self.assertEqual(
                        response_seguindo.request['PATH_INFO'],
                        '/',
                        msg= 'O usuario logado mas é uma empresa, deveria ir para pagina de boas vindas, algo aconteceu aqui, vindo de visualizando pefil.'
                    )
                
                    # Para verificar se esta sendo redirecionada corretamente
                    self.assertEqual(
                        response_seguindo.status_code,
                        200,
                        msg='O status code de boas vindas apos redirecinamento de visualizando pefil não é 200'
                    )
            
                    # Para verificar se view esta com o status code correto
                    self.assertEqual(
                        response.status_code,
                        302,
                        msg='O status code da view visualizando pefil está errado, deveria ser 302, apos ser redirecionado.'
                    )

                elif candidato:
                    #If para validar o redirecionamento da view caso o candidato não tenha perfil
                    if not perfil:
                        # Para preparar o client com login
                        self.c.login(email=self.user_sem_perfil.email, password='Apesar de voce, 4m4nh4')
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('visualizandoperfil'), follow=True)
                        response = self.c.get(reverse('visualizandoperfil'))
                            
                        # Para ver se está na url certa
                        self.assertEqual(
                            response_seguindo.request['PATH_INFO'],
                            '/candidato/criandoperfil',
                            msg= 'O candidato sem perfil, deveria ir para pagina de criando perfil, algo aconteceu aqui, vindo de visualizando perfil.'
                        )
                    
                        # Para verificar se esta sendo redirecionada corretamente
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code de criando perfil apos redirecinamento de visualizando perfil não é 200'
                        )
                
                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response.status_code,
                            302,
                            msg='O status code da view visualizando perfil não é 302'
                        )
                                
                    elif perfil:
                        # Para preparar o client com login
                        self.c.login(email=self.user_com_perfil.email, password='Caramujo, e marujos 4m4nh4')
                        #Para instaciar o client a pagina com login
                        response_seguindo = self.c.get(reverse('visualizandoperfil'), follow=True)

                        # Para ver se está na url certa
                        self.assertEqual(
                            response.request['PATH_INFO'],
                            '/candidato/visualizandoperfil',
                            msg= 'A url da view visualizando perfil logado e com perfil, está com erro.'
                        )

                        # Para verificar se as templates que a view usa está certo 
                            #base.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'base.html',
                            msg_prefix= 'A template base.html na view visualizando perfil está com erro.'
                        )

                            #partials/_sidebar.html.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'partials/_sidebar.html',
                            msg_prefix= 'A template _sidebar.html na view visualizando perfil está com erro.'
                        )

                            # visualizandoperfil.html
                        self.assertTemplateUsed(
                            response_seguindo,
                            'candidato/visualizandoperfil.html',
                            msg_prefix= 'A template visualizandoperfil.html na view visualizando perfil está com erro.'
                        )

                        # Para verificar se view esta com o status code correto
                        self.assertEqual(
                            response_seguindo.status_code,
                            200,
                            msg='O status code da view visualizando perfil logado e com perfil, está errado'
                        )
                        
                    perfil = True
        
            logado = True
            validador -= 1
    
    ## FIM test_visualizandoperfil_view

