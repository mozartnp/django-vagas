import random
import json

from django.test import TestCase
from django.contrib.auth import hashers

from user.models import User

class UserModelTestCase(TestCase):
    # Fixture para pre popular o banco de dados
    fixtures  = ['test_user.json']

    def setUp(self):
        self.usuario_criado = User.objects.create(
            email = 'candidato@can.com',
            password = 'A12345678', 
            tipo_user = 'CAND',
        )
        self.usuario_criado.password = hashers.make_password(self.usuario_criado.password)
        self.usuario_criado.save()

    def test_user_registrado(self):
        ''' 
        Teste para ver se o usuario está inserido corretamente no banco
        '''

        # O teste define 5 usuarios aleatoriamente para testar
        contador = 5
        lista_pk =[]
        while contador > 0:
            aleatoria_pk = random.randrange(start=1, stop=User.objects.all().count())
            lista_pk.append(aleatoria_pk)
            contador -= 1
        lista_pk.sort()
        
        # Dados original para confrontar o banco
        with open('./apps/user/fixtures/test_user.json', 'r') as f:
            dados = json.load(f)

        for dado in dados: 
            if dado["pk"] in lista_pk:
                pk_checagem = dado["pk"]
                usuario = User.objects.get(pk=pk_checagem)

                # Aqui server para arrumar o hasher do password, pois quando passa pela fixture, a senha não passa por processo de criptografia
                # Não faço a melhorar para todos as senhas pois consome muito recurso, assim fica mais eficiente... 
                usuario.password = hashers.make_password(usuario.password)
                usuario.save()

                self.assertEqual(usuario.check_password(dado["fields"]["password"]), True, msg='A senha {} está com erro'.format(usuario.email))
                self.assertEqual(usuario.email, dado["fields"]["email"], msg='O email do usuario {} está com erro'.format(usuario.email))
                self.assertEqual(usuario.tipo_user, dado["fields"]["tipo_user"], msg='O tipo do usuario {} está com erro'.format(usuario.email))
                self.assertEqual(usuario.is_active, dado["fields"]["is_active"], msg='O campo de is_active {} está com erro'.format(usuario.email))
                self.assertEqual(usuario.is_admin, dado["fields"]["is_admin"], msg='O campo de is_admin {} está com erro'.format(usuario.email))
                self.assertEqual(usuario.is_staff, dado["fields"]["is_staff"], msg='O campo de is_staff {} está com erro'.format(usuario.email))
                self.assertEqual(usuario.is_superuser, dado["fields"]["is_superuser"], msg='O campo de is_superuser {} está com erro'.format(usuario.email))  

    def test_cadastro_user(self):
        '''
        Teste para ver se o usuario é criado pelo django        
        '''
        usuario_cria = User.objects.get(email=self.usuario_criado)
   
        self.assertEqual(usuario_cria.check_password('A12345678'), True, msg='A senha do usuario criado está errada.')
        self.assertEqual(usuario_cria.tipo_user,'CAND', msg='O tipo do usuario criado está com erro')
        self.assertEqual(usuario_cria.is_active, True, msg='O campo de is_active do usuario criado está com erro')
        self.assertEqual(usuario_cria.is_admin, False, msg='O campo de is_admin do usuario criado está com erro')
        self.assertEqual(usuario_cria.is_staff, False, msg='O campo de is_staff do usuario criado está com erro')
        self.assertEqual(usuario_cria.is_superuser, False, msg='O campo de is_superuser do usuario criado está com erro')
