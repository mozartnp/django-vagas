# from django.test import LiveServerTestCase, Client
# from selenium import webdriver

# import time

# class CandidatoTestCase(LiveServerTestCase):

#     #Para setar o navegador
#     def setUp(self): 
#         self.browser = webdriver.Firefox(executable_path='./geckodriver')

#     #Para fechar o navegador
#     def tearDown(self):
#         self.browser.quit()

#     # Testes funcionais candidato
#     def test_cadastro_novo_candidato(self):
#         ''' 
#         Teste para cadastrar um novo colaborador
#         '''
#         # instanciar o client
#         c = Client()

#         # Abre a pagina de cadastro do colaborador
#         resposta = c.post('/candidato/cadastrocandidato')
#         self.assertEqual(resposta.status_code, 200, msg="A pagina não foi encontrada")

#         self.browser.get(self.live_server_url + '/candidato/cadastrocandidato')

#         # Confere o titulo da pagina se é Cadastro de Candidatos
#         self.assertEqual(
#             self.browser.title ,
#             'Cadastro de Candidatos',
#             msg='O titulo da pagina não condiz com "Cadastro de Candidatos".'
#         )

#         # O candidato lê o anuncio da pagina, lê ele e se interessa para se inscrever 
#         anuncio = self.browser.find_element_by_css_selector('section[data-info="cadastroCandidatoAnuncio"')
#         self.assertEqual(
#             anuncio.text,
#             'Cadastre-se na nossa plataforma de empregos.\nA maior plataforma de empregos em Django do Brasil.',
#             msg='O anuncio está diferente do definido:\nCadastre-se na nossa plataforma de empregos.\nA maior plataforma de empregos em Django do Brasil.'
#         )

#         # Procura o formulario para cadastro
#         self.assertTrue(self.browser.find_element_by_css_selector('form[data-info="cadastroCandidatoForm"'))
        
        

