from django.test import TestCase

from empresa.forms.info_form import InfoForm
from empresa.forms.vaga_form import VagaForm

from user.models import User

class InfoFormsTestCase(TestCase):
    
    def test_info_form_passa_nao_passa(self):
        '''
        Teste para ver se o form info da empresa está passando, ou não os campos determinados.
        '''
        form = InfoForm()
        
        # Parte para garanti que os campos passe no form
        self.assertIn(
            "nome_empresa", 
            form.fields, 
            msg="O campo nome empresa deveria passar no form."
        )
        self.assertIn(
            "telefone_empresa", 
            form.fields, 
            msg="O campo telefone da empresa deveria passar no form."
        )
        self.assertIn(
            "contato_empresa", 
            form.fields, 
            msg="O campo contato empresa deveria passar no form."
        )
       
        # Para que garanti que certos campos do model não passem no form
        self.assertNotIn(
            'user', 
            form.fields, 
            msg="O campo user não deveria passar no form."
        )
        self.assertNotIn(
            'slug', 
            form.fields, 
            msg="O campo slug não deveria passar no form."
        )

    # FIM test_cadastro_user_form_passa_nao_passa

    def test_info_form_valid(self):
        '''
        Para testar se o form info da empresa, está valido
        '''
        self.empresa_com_info = User.objects.create(
            email= "sono@damulesta.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )

        form_valido = InfoForm(
            data={
                'nome_empresa' : "Azul é mais quente",
                'telefone_empresa' : "(81) 9.9999-9999",
                'contato_empresa' : "Marcelinho",
                'user_id' : self.empresa_com_info.id,
            }
        )
        form_invalido = InfoForm(
            data={
                'nome_empresa' : "",
                'telefone_empresa' : "",
                'contato_empresa' : "",
                'user_id' : "",
            }
        )
        self.assertTrue(form_valido.is_valid())
        self.assertFalse(form_invalido.is_valid())

    ## FIM test_perfil_form_valid

    def test_vaga_form_passa_nao_passa(self):
        '''
        Teste para ver se o form vaga da empresa está passando, ou não os campos determinados.
        '''
        form = VagaForm()
        
        # Parte para garanti que os campos passe no form
        self.assertIn(
            "nome_vaga",
            form.fields, 
            msg="O campo nome vaga deveria passar no form."
        )
        self.assertIn(
            "faixa_salario", 
            form.fields, 
            msg="O campo faixa salario deveria passar no form."
        )
        self.assertIn(
            "nivel_escolaridade", 
            form.fields, 
            msg="O campo nivel escolaridade deveria passar no form."
        )
        self.assertIn(
            "requisitos", 
            form.fields, 
            msg="O campo requisitos deveria passar no form."
        )
       
        # Para que garanti que certos campos do model não passem no form
        self.assertNotIn(
            'user', 
            form.fields, 
            msg="O campo user não deveria passar no form."
        )
        self.assertNotIn(
            'slug', 
            form.fields, 
            msg="O campo slug não deveria passar no form."
        )

    # FIM test_vaga_form_passa_nao_passa

    def test_vaga_form_valid(self):
        '''
        Para testar se o form vaga da empresa, está valido
        '''
        self.empresa_com_info = User.objects.create(
            email= "sonoaa@damulesta.com",
            password= "CANSEI DE criar SENHAS NOVAS AGORA É SÓ ESSA 555 @:@:@:@:",
            tipo_user= "EMPR"
        )

        form_valido = VagaForm(
            data={
                'nome_vaga' : "Python Jr",
                'faixa_salario' : ">3k",
                'nivel_escolaridade' : "doutorado",
                'requisitos' : "Estudar muito",
                'user_id' : self.empresa_com_info.id,
            }
        )
        form_invalido = VagaForm(
            data={
                'nome_vaga' : "",
                'faixa_salario' : "",
                'nivel_escolaridade' : "",
                'requisitos' : "",
                'user_id' : self.empresa_com_info.id,
            }
        )
        self.assertTrue(form_valido.is_valid())
        self.assertFalse(form_invalido.is_valid())

    ## FIM test_vaga_form_valid