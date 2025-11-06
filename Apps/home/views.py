from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UserCreationForm, RegistroForm



# Create your views here.

class HomeView(TemplateView):
    template_name= 'home.html'

class loginView(TemplateView):
    template_name= 'login.html'

class listar_guiasView(TemplateView):
    template_name= 'listar_guias.html'

class crear_guiaView(TemplateView):
    template_name= 'crear_guia.html'

class detalle_guiaView(TemplateView):
    template_name= 'detalle_guia.html' 
    
class registerView(TemplateView):
    template_name= 'register.html'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda automáticamente en SQLite3
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada exitosamente para {username}')
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('login')
