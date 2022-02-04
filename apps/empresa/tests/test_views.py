from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import hashers

from empresa.views.info_views import cadastrandoinfo
from empresa.models.info_model import InfoModel

from candidato.models.perfil_models import PerfilModel

from user.models import User

class TestInfoViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.empresa_sem_info = User.objects.create(
            email= "testasde@testando.com",
            password= "Apesar de voce, 4m4nh4",
            tipo_user= "EMPR"
        )
        # Atualizar o hashers do passaword
        self.empresa_sem_info.password = hashers.make_password(self.empresa_sem_info.password)
        self.empresa_sem_info.save()

        self.candidao_errado = User.objects.create(
            email= "lugar@errado.com",
            password= "Apesar de voce, 4m4nh4",
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

        # #Criando um novo usuario com perfil
        # self.user_com_perfil = User.objects.create(
        #     email= "testando@teste.com",
        #     password= "Apesar de voce, 4m4nh4",
        #     tipo_user= "CAND"
        # )




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
                    self.c.login(email=self.candidao_errado.email, password="Apesar de voce, 4m4nh4")
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
                    self.c.login(email=self.empresa_sem_info.email, password="Apesar de voce, 4m4nh4")
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

    ## FIM test_criandoperfil_view