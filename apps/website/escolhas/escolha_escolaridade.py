from django.db import models
from django.utils.translation import gettext_lazy as _

class NivelEscolaridade(models.TextChoices):
    '''
    Escolha de escolaridade, mudar aqui irá impactar tanto na criação de vagas, como de perfil. 
    Lembresse tirar alguma informação aqui pode impactar cadastros já feitos.
    '''
    FUNDAMENTAL = 'fundamental', _('Ensino fundamental')
    MEDIO = 'medio', _('Ensino médio')
    TECNOLOGO = 'tecnologo', _('Tecnólogo')
    SUPERIOR = 'superior', _('Ensino superior')
    POS = 'pos', _('Pós / MBA / Mestrado')
    DOUTORADO = 'doutorado', _('Doutorado')
