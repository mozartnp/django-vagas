from django.urls import path 
from .views import *

urlpatterns = [
    path('cadastrandoinfo', cadastrandoinfo, name='cadastrandoinfo'),
]