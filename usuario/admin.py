from django.contrib import admin
from .models import Cliente, Tecnico

# Register your models here.
@admin.register(Cliente)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'criado',
    )

@admin.register(Tecnico)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'criado',
    )