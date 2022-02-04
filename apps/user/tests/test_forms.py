from django.test import TestCase

from user.forms import CadastroUser

class UserFormsTestCase(TestCase):
    
    def test_cadastro_user_form_passa_nao_passa(self):
        '''
        Teste para ver se o form está passando, ou não os campos determinados.
        '''
        form = CadastroUser()
        
        # Parte para garanti que os campos passe no form
        self.assertIn(
            "email", 
            form.fields, 
            msg="Erro no campo email no django form."
        )
        self.assertIn(
            "tipo_user", 
            form.fields, 
            msg="Erro no campo tipo_user no django form."
        )
        self.assertIn(
            "password1", 
            form.fields, 
            msg="Erro no campo password1 no django form."
        )
        self.assertIn(
            "password2", 
            form.fields, 
            msg="Erro no campo password2 no django form."
        )
        # Para que garanti que certos campos do model não passem no form
        self.assertNotIn(
            'date_joined', 
            form.fields, 
            msg="O campo date_joined não deveria passar."
        )
        self.assertNotIn(
            'last_login', 
            form.fields, 
            msg="O campo last_login não deveria passar."
        )
        self.assertNotIn(
            'is_active', 
            form.fields, 
            msg="O campo is_active não deveria passar."
        )
        self.assertNotIn(
            'is_admin', 
            form.fields, 
            msg="O campo is_admin não deveria passar."
        )
        self.assertNotIn(
            'is_staff', 
            form.fields, 
            msg="O campo is_staff não deveria passar."
        )
        self.assertNotIn(
            'is_superuser', 
            form.fields, 
            msg="O campo is_superuser não deveria passar."
        )
  
    ## FIM test_cadastro_user_form_passa_nao_passa
    
    def test_cadastro_user_form_valid(self):
        '''
        Para testar se o form cadastro user, está valido
        '''
        form_valido = CadastroUser(
            data={
                'email' : "tibia@fibula.com",
                'tipo_user' : "CAND",
                'password1' : "J040 e M4R14 querem doce",
                'password2' : "J040 e M4R14 querem doce",
            }
        )
        form_invalido = CadastroUser(
            data={
                'email' : "",
                'tipo_user' : "",
                'password1' : "",
                'password2' : "",
            }
        )
        self.assertTrue(form_valido.is_valid())
        self.assertFalse(form_invalido.is_valid())

