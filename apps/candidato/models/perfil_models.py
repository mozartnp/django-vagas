from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save

from website.escolhas.escolha_escolaridade import  NivelEscolaridade
from website.escolhas.escolha_salario import FaixaSalario

class PerfilModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_candidato = models.CharField(max_length=60)
    telefone_candidato = models.CharField(max_length=60, null=True)
    faixa_salario = models.CharField(max_length=7,choices=FaixaSalario.choices)
    nivel_escolaridade = models.CharField(max_length=11,choices=NivelEscolaridade.choices)
    experiencia = models.TextField()
    ultima_modificacao = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)

# Essa função é para antes de salvar, vê se tem slug, e cria-lo.
def pre_save_perfil(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify('perfil' + '-' + instance.nome_candidato)

# Para ativar o slug
pre_save.connect(pre_save_perfil, sender=PerfilModel)