from django.contrib import admin
from .models import Chamado

# Register your models here.

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    '''Admin View for Chamado'''

    list_display = (
        'numero',
        'cliente',
        'titulo',
        'descricao',
        'prioridade',
        'estado',
        'criado',
        'modificado',
        'tecnico',
        'nota_de_fecho',
        
        )