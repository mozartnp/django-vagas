from django.shortcuts import render

def cadastro_candidato(request):
    return render(request, 'candidato/cadastrocandidato.html')