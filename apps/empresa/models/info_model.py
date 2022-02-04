from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save

class InfoModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_empresa = models.CharField(max_length=60)
    telefone_empresa = models.CharField(max_length=60, null=True)
    contato_empresa = models.CharField(max_length=60, null=True)
    slug = models.SlugField(blank=True, unique=True)

# Essa função é para antes de salvar, vê se tem slug, e cria-lo.
def pre_save_info(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify('info' + '-' + instance.nome_empresa)

# Para ativar o slug
pre_save.connect(pre_save_info, sender=InfoModel)

# from website.models import escolha_salario, escolha_escolaridade
# faixa_salario = models.CharField(max_length=7,choices=escolha_salario.FaixaSalario.choices)
# nivel_escolaridade = models.CharField(max_length=11,choices=escolha_escolaridade.NivelEscolaridade.choices)