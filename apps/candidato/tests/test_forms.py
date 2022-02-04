from django.test import TestCase

from candidato.forms.perfil_forms import PerfilForm

from user.models import User

class PerfilFormsTestCase(TestCase):
    
    def test_perfil_form_passa_nao_passa(self):
        '''
        Teste para ver se o form está passando, ou não os campos determinados.
        '''
        form = PerfilForm()
        
        # Parte para garanti que os campos passe no form
        self.assertIn(
            "nome_candidato", 
            form.fields, 
            msg="O campo nome candidato deveria passar no form."
        )
        self.assertIn(
            "telefone_candidato", 
            form.fields, 
            msg="O campo telefone do candidato deveria passar no form."
        )
        self.assertIn(
            "faixa_salario", 
            form.fields, 
            msg="O campo faixa de salario deveria passar no form."
        )
        self.assertIn(
            "nivel_escolaridade", 
            form.fields, 
            msg="O nivel de escolaridade deveria passar no form."
        )
        self.assertIn(
            "experiencia", 
            form.fields, 
            msg="O campo experiencia deveria passar no form."
        )
       
        # Para que garanti que certos campos do model não passem no form
        self.assertNotIn(
            'user', 
            form.fields, 
            msg="O campo user não deveria passar no form."
        )
        self.assertNotIn(
            'ultima_modificacao', 
            form.fields, 
            msg="O campo ultima modificação não deveria passar no form."
        )
        self.assertNotIn(
            'slug', 
            form.fields, 
            msg="O campo slug não deveria passar no form."
        )

    ## FIM test_cadastro_user_form_passa_nao_passa

    def test_perfil_form_valid(self):
        '''
        Para testar se o form perfil candidato, está valido
        '''
        user_com_perfil = User.objects.create(
            email= "zumba@bol.com",
            password= "Meteu essa @asd 69",
            tipo_user= "CAND"
        )
        form_valido = PerfilForm(
            data={
                'nome_candidato' : "Azul é mais quente",
                'telefone_candidato' : "(81) 9.9999-9999",
                'faixa_salario' : "<1k_2k>",
                'nivel_escolaridade' : "doutorado",
                'experiencia' : "Tudo e um pouco mais.",
                'user_id' : user_com_perfil.id,
            }
        )
        form_invalido = PerfilForm(
            data={
                'nome_candidato' : "",
                'telefone_candidato' : "",
                'faixa_salario' : "",
                'nivel_escolaridade' : "",
                'experiencia' : "",
                'user_id' : "",
            }
        )
        self.assertTrue(form_valido.is_valid())
        self.assertFalse(form_invalido.is_valid())

    ## FIM test_perfil_form_valid