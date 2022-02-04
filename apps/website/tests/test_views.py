from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import hashers

from website.views import boasvindas_views, cadastro_views, login_views, logout

from candidato.views.perfil_views import visualizandoperfil
from candidato.models.perfil_models import PerfilModel

from user.forms import CadastroUser
from user.models import User

class TestWebsiteViews(TestCase):

    def setUp(self):
        self.c = Client()
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
    
    ## FIM setUp

    def test_boasvindas_view(self):
        '''
        Teste da view da boas vindas
        '''
        response = self.c.get(reverse('boasvindas'), follow=True)
        # Para ver se está na url certa
        self.assertEqual(
            response.request['PATH_INFO'],
            '/',
            msg= 'A url da pagina boas vindas está com erro.'
        )

        # Para verificar se as templates que a view usa está certo 
            #base.html
        self.assertTemplateUsed(
            response,
            'base.html',
            msg_prefix= 'A template base.html na pagina boas vindas está com erro.'
        )

            #_navbar.html
        self.assertTemplateUsed(
            response,
            'partials/_navbar.html',
            msg_prefix= 'A template _navbar.html na pagina boas vindas está com erro.'
        )

            #boasvindas.html
        self.assertTemplateUsed(
            response,
            'website/boasvindas.html',
            msg_prefix= 'A template boasvindas.html na pagina boas vindas está com erro.'
        )

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(
            response.status_code,
            200,
            msg='O status code da pagina boas vindas está errado'
        )

    ## FIM de test_boasvindas_view 

    def test_cadastro_view(self):
        '''
        Teste da view do cadastro de usuario
        '''
        response = self.c.get(reverse('cadastro'), follow=True)
        # Para ver se está na url certa
        self.assertEqual(
            response.request['PATH_INFO'],
            '/cadastro',
            msg= 'A url da pagina cadastro está com erro.'
        )
        
        # Para verificar se as templates que a view usa está certo 
            #base.html
        self.assertTemplateUsed(
            response,
            'base.html',
            msg_prefix= 'A template base.html na pagina cadastro está com erro.'
        )

            #_navbar.html
        self.assertTemplateUsed(
            response,
            'partials/_navbar.html',
            msg_prefix= 'A template _navbar.html na pagina cadastro está com erro.'
        )

            #cadastro.html
        self.assertTemplateUsed(
            response,
            'website/cadastro.html',
            msg_prefix= 'A template cadastro.html na pagina cadastro está com erro.'
        )

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(
            response.status_code,
            200,
            msg='O status code da pagina cadastro está errado'
        )

    ## FIM de test_cadastro_view

    def test_inserindoCadastro_view(self):
        '''
        Teste da view inserindo Cadastro 
        '''
        form_post ={
            'email' : "tibia@fibula.com",
            'tipo_user' : "CAND",
            'password1' : "J040 e M4R14 querem doce",
            'password2' : "J040 e M4R14 querem doce",
        }
        response_seguindo = self.c.post(reverse('inserindoCadastro'), data=form_post, follow=True)
        response = self.c.post(reverse('inserindoCadastro'),data=form_post)

        # Para ver se a url esta indo para o lugar certo
        self.assertEqual(
            response_seguindo.request['PATH_INFO'],
            '/candidato/criandoperfil',
            msg= 'Como foi um cadastro de candidato ele deveria ser redirecinado para a pagina criando perfil'
        )               
        
        # Para verificar se esta sendo redirecionada corretamente
        self.assertEqual(
            response_seguindo.status_code,
            200,
            msg='O status code da nova view acessada apos redirecinamento de inserindo cadastro não é 200.'
        )

        # Para verificar se view esta com o status code correto
        self.assertEqual(
            response.status_code,
            302,
            msg='O status code da view inserindo cadastro está errado, deveria ser 302, apos ser redirecionado.'
        )

    ## FIM de test_inserindoCadastro_view

    def test_login_view(self):
        '''
        Teste da view do login
        '''
        response = self.c.get(reverse('login'), follow=True)
        # Para ver se está na url certa
        self.assertEqual(
            response.request['PATH_INFO'],
            '/login',
            msg= 'A url da pagina login está com erro.'
        )

       # Para verificar se as templates que a view usa está certo 
            #base.html
        self.assertTemplateUsed(
            response,
            'base.html',
            msg_prefix= 'A template base.html na pagina login está com erro.'
        )

            #_navbar.html
        self.assertTemplateUsed(
            response,
            'partials/_navbar.html',
            msg_prefix= 'A template _navbar.html na pagina login está com erro.'
        )

            #login.html
        self.assertTemplateUsed(
            response,
            'website/login.html',
            msg_prefix= 'A template login.html na pagina login está com erro.'
        )

        # Para verificar se view esta sendo acessada corretamente
        self.assertEqual(
            response.status_code,
            200,
            msg='O status code da pagina login está errado'
        )

    ## FIM de test_login_view

    def test_logout_view(self):
        '''
        Teste da view de logout
        '''
        # Para preparar o client com login
        self.c.login(email=self.user_com_perfil.email, password='Caramujo, e marujos 4m4nh4')
        # Para instaciar o client a pagina com login 
        # Aqui vou primeiro em uma outra pagina logado, no caso visualizando perfil, e lá irei desolgar
        response_seguindo = self.c.get(reverse('visualizandoperfil'), follow=True)

        # Para ver se está na url certa
        self.assertEqual(
            response_seguindo.request['PATH_INFO'],
            '/candidato/visualizandoperfil',
            msg= 'A url da view visualizando perfil logado e com perfil, está com erro.'
        )
        # Para verificar se view esta com o status code correto
        self.assertEqual(
            response_seguindo.status_code,
            200,
            msg='O status code da view visualizando perfil logado e com perfil, está errado'
        )

        # Uma vez logado agora irei deslogar o usuario. 
        response_seguindo = self.c.get(reverse('logout'), follow=True)

        # Para ver se está na url certa
        self.assertEqual(
            response_seguindo.request['PATH_INFO'],
            '/',
            msg= 'A url da view visualizando perfil logado e com perfil, está com erro.'
        )
        # Para verificar se view esta com o status code correto
        self.assertEqual(
            response_seguindo.status_code,
            200,
            msg='O status code da view visualizando perfil logado e com perfil, está errado'
        )

        
    ## FIM test_logout_view