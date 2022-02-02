from django import forms

from candidato.models.perfil_models import PerfilModel

class PerfilForm(forms.ModelForm):

    class Meta:
        model = PerfilModel
        fields = (
            'nome_candidato',
            'telefone_candidato',
            'faixa_salario',
            'nivel_escolaridade',
            'experiencia'
        )
        exclude = ["user"]
        labels = {
            'nome_candidato' : 'Seu nome',
            'telefone_candidato' : 'Telefone para contato',
            'faixa_salario' : 'Expectativa salarial',
            'nivel_escolaridade' : 'Nível de escolaridade',
            'experiencia' : 'Suas experiências'
        }
        widgets= {
            'nome_candidato' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu nome completo.',
                }
            ),
            'telefone_candidato' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite um telefone com DDD para contato.',
                }
            ),
            'experiencia' : forms.Textarea(
                attrs={
                    'placeholder': 'Fale um pouco sobre suas experiências na área.',
                }
            ),
        }