from django.db import models
from django.conf import settings

from candidato.models.perfil_models import PerfilModel

from empresa.models.vaga_model import VagaModel

class VagaEscolhida(models.Model):

    candidato = models.ForeignKey('candidato.PerfilModel', on_delete=models.DO_NOTHING)
    vaga = models.ForeignKey('empresa.VagaModel', on_delete=models.DO_NOTHING)
    pontuacao = models.PositiveSmallIntegerField(default=0)
    escolhido =models.BooleanField(default=False)
    data_candidatura = models.DateTimeField(auto_now_add=True)
