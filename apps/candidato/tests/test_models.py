from django.test import TestCase
from django.contrib.auth import hashers

from candidato.models.perfil_models import PerfilModel

from user.models import User

class TestCandidatoModel(TestCase):


    def setUp(self):
        self.user_com_perfil = User.objects.create(
            email= "doido@bol.com",
            password= "AFF 5asd5aas",
            tipo_user= "CAND"
        )
        # Atualizar o hashers do passaword
        self.user_com_perfil.password = hashers.make_password(self.user_com_perfil.password)
        self.user_com_perfil.save()

        self.perfil_user = PerfilModel.objects.create(
            nome_candidato= "Vampiro Doidao",
            telefone_candidato= "(81) 1.1234-8765",
            faixa_salario= "<1k_2k>",
            nivel_escolaridade= "doutorado",
            experiencia= "Voador",
            user_id= self.user_com_perfil.id,
        )
    def test_Perfil_model(self):
        '''
        Teste para ver se o model está reagindo certo a informações escritas nele.
        '''
        usuario = User.objects.get(email="doido@bol.com")
        perfil = PerfilModel.objects.get(pk=usuario.id)

        self.assertEqual(
            perfil.nome_candidato, 
            self.perfil_user.nome_candidato,
            msg="O model não gravou certo o nome do candidato"
        )

        self.assertEqual(
            perfil.telefone_candidato, 
            self.perfil_user.telefone_candidato,
            msg="O model não gravou certo o telefone do candidato"
        )

        self.assertEqual(
            perfil.faixa_salario, 
            self.perfil_user.faixa_salario,
            msg="O model não gravou certo a faixa salarial do candidato"
        )

        self.assertEqual(
            perfil.nivel_escolaridade, 
            self.perfil_user.nivel_escolaridade,
            msg="O model não gravou certo o nivel de escolaridade do candidato"
        )

        self.assertEqual(
            perfil.experiencia, 
            self.perfil_user.experiencia,
            msg="O model não gravou certo a experiencia do candidato"
        )

