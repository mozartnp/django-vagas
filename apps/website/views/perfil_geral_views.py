from django.shortcuts import get_object_or_404, render, redirect

from candidato.models.perfil_models import PerfilModel

from empresa.models.vaga_model import VagaModel

from website.escolhas.escolha_escolaridade import  NivelEscolaridade
from website.escolhas.escolha_salario import FaixaSalario
from website.models.vaga_geral_model import VagaEscolhida

def perfilCandidato(request, id_vaga, id_perfil):
    # If para verificar se o usuario está logado, caso não redireciona ele para a tela de login
    if request.user.is_authenticated:
        vaga_obj = VagaModel.objects.get(pk=id_vaga)
        perfil_obj = PerfilModel.objects.get(pk=id_perfil)
        vaga_escolhida_obj = VagaEscolhida.objects.filter(candidato=perfil_obj.id, vaga=vaga_obj.id)
        salario = FaixaSalario(perfil_obj.faixa_salario).label
        escolaridade = NivelEscolaridade(perfil_obj.nivel_escolaridade).label
        
        contexto={
            'vaga' : vaga_obj,
            'perfil' : perfil_obj,
            'vaga_escolhida' : vaga_escolhida_obj,
            'salario' : salario,
            'escolaridade' : escolaridade,
        }

        return render(request, 'website/perfilcandidato.html', contexto)  

    return redirect (login)