from django.db import models

# Create your models here.
class Meta(models.Model):
    criado = models.DateTimeField(("Criado"), auto_now_add=True)
    modificado = models.DateTimeField(("Modificado"), auto_now=True)
    class Meta:
        abstract = True