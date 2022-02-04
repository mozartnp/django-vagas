from django.test import TestCase, Client
from django.urls import reverse

from website.views import boasvindas_views, cadastro_views, login_views

from user.forms import CadastroUser
from user.models import User

class TestWebsiteViews(TestCase):

    def setUp(self):
        self.c = Client()

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

        ## Fim de test_boasvindas_view 

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

        ## Fim de test_cadastro_view

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

        ## Fim de test_login_view

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

        print()   
        print("###1 ", response.request)
        print("###2 ", response)
        print()
        print("###3 ", response_seguindo.request)
        print("###4 ", response_seguindo)
        print("###5 ", response_seguindo.redirect_chain)

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

        ## Fim de test_inserindoCadastro_view
       