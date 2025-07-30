from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from datetime import datetime
from django.urls import reverse_lazy
from .forms import CreateChamadoForm, EditChamadoForm
from .classes import ChamadoClass
from usuario.models import Tecnico, Cliente
from .models import Chamado

# Create your views here.
class HomeChamadoView(TemplateView):
    template_name = 'home.html'


class CreateChamadoView(CreateView):
    template_name = 'form_create_chamado.html'
    form_class = CreateChamadoForm

    def form_valid(self, form):
    		#u = self.request.user.cliente

		#===========Geração do número de chamado=========
	    chamado_obj = ChamadoClass()
	    numero = chamado_obj.numero_chamado
	    data = datetime.now()
		#usuario = self.request.user.pk
		#numero = random.randint(1000, 100000)
	    data_str = data.strftime('%d%m%Y%H%M%S')
	    numero_chamado = data_str + str(numero)
		#================================================

		#===========Pegar cliente logado no sistema e Técnico Padrão=========
		
	    tecnico = Tecnico.objects.filter().get(pk=1)
	    cliente = self.request.user.cliente
		#====================================================

		#================Inserir dados anterior no Chamado============
	    form.instance.cliente = cliente
	    form.instance.tecnico = tecnico 
	    form.instance.numero = numero_chamado
		#================================================
	    url = super().form_valid(form)

	    return url
    success_url = reverse_lazy('chamado:read')


class ReadChamadoView(ListView):
	template_name = 'table_read_chamado.html'
	model = Chamado
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['object_list'] = self.object_list = Chamado.objects.all()
		context['table'] = 'TODOS CHAMADOS'

		return context

class ReadOpenChamadoView(ListView):
	template_name = 'table_read_chamado.html'
	model = Chamado
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['object_list'] = self.object_list = Chamado.objects.filter(estado = 'Aberto')
		context['table'] = 'CHAMADOS ABERTOS'

		return context


class ReadClosedChamadoView(ListView):
	template_name = 'table_read_chamado.html'
	model = Chamado
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['object_list'] = self.object_list = Chamado.objects.filter(estado = 'Fechado')
		context['table'] = 'CHAMADOS FECHADOS'

		return context

class EditChamadoView(UpdateView):
	template_name = 'form_edit_chamado.html'
	model = Chamado
	form_class = EditChamadoForm
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		tecnico = Tecnico.objects.all()

		context['tecnico'] = tecnico

		return context

	success_url = reverse_lazy('chamado:read')


class DeleteChamadoView(DeleteView):
	pass

"""
class CloseChamadoView(UpdateView):
	template_name = 'frm_close_chamado.html'
	model = Chamado
	fields = [
	'estado',
	'nota_de_fecho'
	]
	
	success_url = reverse_lazy('chamado:read')


class OpenAgainChamadoView(UpdateView):
	template_name = 'frm_open_chamado.html'
	model = Chamado
	fields = [
	'estado',
	'nota_de_fecho'
	]

	success_url = reverse_lazy('chamado:read')
"""
class OwnerChamadoView(UpdateView):
	template_name = 'frm_owner_chamado.html'
	model = Chamado
	fields = [
	'tecnico'
	]

	success_url = reverse_lazy('chamado:read')

class MudarEstadoChamadoView(UpdateView):
    template_name = 'frm_estado_chamado.html'
    model = Chamado
    fields = [
	'estado',
	'nota_de_fecho'
	]
	
    success_url = reverse_lazy('chamado:home')

class HomeChamadoView(TemplateView):
    template_name = 'home.html'
    model = Chamado

    def get_context_data(self, *args, **kwargs):
        contexto = super().get_context_data(*args, **kwargs)
        contexto = {
            'todo':Chamado.objects.filter(estado = 'Aberto', tecnico=self.request.user.tecnico),
            'doing':Chamado.objects.filter(estado = 'Tratando', tecnico=self.request.user.tecnico),
            'done':Chamado.objects.filter(estado = 'Fechado', tecnico=self.request.user.tecnico),
        }

        return contexto
