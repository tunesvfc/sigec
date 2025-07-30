from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy

from chamado.models import Chamado

# Create your views here.
class IndexCoreView(TemplateView):
    template_name = 'index.html'


