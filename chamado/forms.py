from django import forms
from django.forms import fields

from .models import Chamado

class CreateChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = [
            'titulo',
			'descricao',
			'prioridade',
        ]


class EditChamadoForm(forms.ModelForm):
    class Meta:
	    model = Chamado
	    fields = [
			'titulo',
			'descricao',
			'prioridade',
			'estado',
			'numero',
			'cliente',
			'tecnico',
		]