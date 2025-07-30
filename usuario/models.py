from core.models import Meta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tecnico(Meta):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return "{} {}".format(self.usuario.first_name, self.usuario.last_name)

class Cliente(Meta):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} {}".format(self.usuario.first_name, self.usuario.last_name)