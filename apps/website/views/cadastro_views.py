from django.shortcuts import render

def cadastro(request):
    return render(request, 'website/cadastro.html')