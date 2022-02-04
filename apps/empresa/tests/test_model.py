from django.test import TestCase
from django.contrib.auth import hashers

from empresa.models.info_model import InfoModel

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