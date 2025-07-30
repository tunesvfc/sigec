from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import CreateUserForm
from .models import Cliente, Tecnico
# Create your views here.

class HomeUsuarioView(TemplateView):
    template_name = 'home.html'


class CreateClienteView(CreateView):
    template_name = 'form_create_user.html'
    form_class = CreateUserForm

    def get_context_data(self, *args,**kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['dado']= 'Registo de Novo Cliente'

        return context

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="cliente")
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Cliente.objects.create(usuario = self.object)

        return url
    
    success_url = reverse_lazy('core:index')


class CreateTecnicoView(CreateView):
    template_name = 'form_create_user.html'
    form_class = CreateUserForm

    def get_context_data(self, *args,**kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['dado']= 'Registo de Novo Técnico'

        return context

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name = "tecnico")
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Tecnico.objects.create(usuario = self.object)

        return url
        
    success_url = reverse_lazy('core:index')


"""
def alterarPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "home.html")
        else:
            return redirect('core:index')
    else:
        form = PasswordChangeForm(user = request.user)
        context = {
            'form':form
        }
    return render(request, "alterarSenha.html", context)


class AlterarPassword(CreateView):
    template_name = 'form_change_password.html'
    form_class = PasswordChange

    success_url = reverse_lazy('usuario:login')

"""