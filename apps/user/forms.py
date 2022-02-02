from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User

class CadastroUser(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'email', 
            'tipo_user',
            'password1',
            'password2'
        )
        labels = {
            'tipo_user' : 'Tipo de cadastro'
        }
        widgets= {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder': 'Digite seu e-mail.',
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(CadastroUser, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Sua senha deve conter A-Z a-z 0-9',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Repita sua senha.',
            }
        )

    # TODO limpar isso?
    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     tipo_user = self.cleaned_data.get('tipo_user')
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     lista_erros= {}
    #     senhas_iguais(password1, password2, lista_erros)

    #     if lista_erros is not None:
    #         for erro in lista_erros:
    #             mensagem_erro = lista_erros[erro]
    #             self.add_error(erro, mensagem_erro)

    #     return self.cleaned_data