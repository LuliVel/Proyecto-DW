from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name= 'home.html'

class loginView(TemplateView):
    template_name= 'login.html'

class registerView(TemplateView):
    template_name= 'register.html'
    
class listar_guiasView(TemplateView):
    template_name= 'listar_guias.html'

class crear_guiaView(TemplateView):
    template_name= 'crear_guia.html'
    
class detalle_guiaView(TemplateView):
    template_name= 'detalle_guia.html'