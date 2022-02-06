from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save

from website.models import escolha_salario, escolha_escolaridade

class VagaModel(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_vaga = models.CharField(max_length=60, unique=True)
    faixa_salario = models.CharField(max_length=7,choices=escolha_salario.FaixaSalario.choices)
    nivel_escolaridade = models.CharField(max_length=11,choices=escolha_escolaridade.NivelEscolaridade.choices)
    requisitos = models.TextField()
    slug = models.SlugField(blank=True, unique=True)

# Essa função é para antes de salvar, vê se tem slug, e cria-lo.
def pre_save_vaga(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.nome_vaga)

# Para ativar o slug
pre_save.connect(pre_save_vaga, sender=VagaModel)