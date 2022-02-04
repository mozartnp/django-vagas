from django.db import models
from django.utils.translation import gettext_lazy as _


class FaixaSalario(models.TextChoices):
    '''
    Escolha de faixa de salario, mudar aqui irá impactar tanto na criação de vagas, como de perfil.
    Lembresse tirar alguma informação aqui pode impactar cadastros já feitos.
    '''
    ABAIXO_1000 = '<1k', _('Até R$1.000,00')
    ENTRE_1000_2000 = '<1k_2k>', _('Entre R$1.000,00 e R$2.000,00')
    ENTRE_2000_3000 = '<2k_3k>', _('Entre R$2.000,00 e R$3.000,00')
    ACIMA_3000 = '>3k', _('Acima de R$3.000,00')