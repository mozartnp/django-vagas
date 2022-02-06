from django.test import TestCase
from django.contrib.auth import hashers

from empresa.models.info_model import InfoModel
from empresa.models.vaga_model import VagaModel

from user.models import User

class TestCandidatoModel(TestCase):


    def setUp(self):
        self.empresa_com_info = User.objects.create(
            email= "sono@damulesta.com",
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

        self.vaga_empresa = VagaModel.objects.create(
            nome_vaga= "Python/django",
            faixa_salario= "<1k_2k>",
            nivel_escolaridade="tecnologo",
            requisitos="Django\nPython\nTDD",
            user_id= self.empresa_com_info.id,
        )

    ## FIM setUp

    def test_Info_model(self):
        '''
        Teste para ver se o model está reagindo certo a informações escritas nele.
        '''
        usuario = User.objects.get(email="sono@damulesta.com")
        info = InfoModel.objects.get(user_id=usuario.id)
        
        self.assertEqual(
            info.nome_empresa, 
            self.info_empresa.nome_empresa,
            msg="O model não gravou certo o nome da empresa."
        )

        self.assertEqual(
            info.telefone_empresa, 
            self.info_empresa.telefone_empresa,
            msg="O model não gravou certo o telefone da empresa."
        )

        self.assertEqual(
            info.contato_empresa, 
            self.info_empresa.contato_empresa,
            msg="O model não gravou certo o contato da empresa"
        )

    ## FIM test_Info_model

    def test_Vaga_model(self):
        '''
        Teste para ver se o model está reagindo certo a informações escritas nele.
        '''
        usuario = User.objects.get(email="sono@damulesta.com")
        vaga = VagaModel.objects.get(user_id=usuario.id)
        
        self.assertEqual(
            vaga.nome_vaga, 
            self.vaga_empresa.nome_vaga,
            msg="O model não gravou certo o nome da vaga."
        )

        self.assertEqual(
            vaga.faixa_salario, 
            self.vaga_empresa.faixa_salario,
            msg="O model não gravou certo a faixa salarial."
        )

        self.assertEqual(
            vaga.nivel_escolaridade, 
            self.vaga_empresa.nivel_escolaridade,
            msg="O model não gravou certo o nivel de escolaridade."
        )

        self.assertEqual(
            vaga.requisitos, 
            self.vaga_empresa.requisitos,
            msg="O model não gravou certo o requisisto."
        )

    ## FIM test_Vaga_model