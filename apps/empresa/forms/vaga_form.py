from django import forms

from empresa.models.vaga_model import VagaModel

class VagaForm(forms.ModelForm):

    class Meta:
        model = VagaModel
        fields = (
            'nome_vaga',
            'faixa_salario',
            'nivel_escolaridade',
            'requisitos'
        )
        labels = {
            'nome_vaga' : "Vaga",
            'faixa_salario' : "Faixa salarial da vaga",
            'nivel_escolaridade' : "Nível de escolaridade",
            'requisitos' : "Requisitos para a vaga",
        }
        widgets= {
            'nome_vaga' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite uma descrição breve da vaga.',
                }
            ),
            'requisitos' : forms.Textarea(
                attrs={
                    'placeholder': 'Quais são os requisitos da vaga.',
                }
            ),
        }