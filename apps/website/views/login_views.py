from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_auth

from .boasvindas_views import boasvindas

def login(request):
    return render(request, 'website/login.html')

def logout(request):
    logout_auth(request)
    return redirect('boasvindas')