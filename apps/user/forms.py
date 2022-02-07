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

class AutencicandoUser(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder' : "Digite seu e-mail"}
        )
    )
    password = forms.CharField(
        label= "Senha",
        widget=forms.PasswordInput(
            attrs={'placeholder' : "Digite sua senha"}
        )
    )
