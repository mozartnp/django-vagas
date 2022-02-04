from django import forms

from empresa.models.info_model import InfoModel

class InfoForm(forms.ModelForm):

    class Meta:
        model = InfoModel
        fields = (
            'nome_empresa',
            'telefone_empresa',
            'contato_empresa',
        )
        labels = {
            'nome_empresa' : 'Nome da empresa',
            'telefone_empresa' : 'Telefone para contato',
            'contato_empresa' : 'Nome do contato',
        }
        widgets= {
            'nome_empresa' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite o nome da empresa.',
                }
            ),
            'telefone_empresa' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite um telefone com DDD para contato.',
                }
            ),
            'contato_empresa' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite o nome de uma pessoa para contato.',
                }
            ),
        }