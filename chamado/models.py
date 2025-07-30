from django.db import models
from usuario.models import Cliente, Tecnico
from core.models import Meta

# Create your models here.
PRIORIDADES = (
    ('Média','Média'),
    ('Baixa','Baixa'),
    ('Alta','Alta'),
    ('Urgente','Urgente'),
)

ESTADOS = (
    ('Aberto','Aberto'),
    ('Tratando','Tratando'),
    ('Fechado','Fechado'),
    ('Morto','Morto'),
)

class Chamado(Meta):
    numero = models.PositiveBigIntegerField("Número do Chamado", null=True)
    titulo = models.CharField(("Título do Chamado"), max_length=100)
    descricao = models.TextField(("Descrição"), max_length = 200)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)
    prioridade = models.CharField(max_length=60, choices=PRIORIDADES, default='Baixa')
    estado = models.CharField(max_length=60, choices=ESTADOS, default='Aberto')
    nota_de_fecho = models.CharField(("Nota de Fecho"), max_length=200, null=True)
    nota_de_atribuicao = models.CharField(("Nota de Atribuição"), max_length=200, null=True)