from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Diario(models.Model):
    conteudo = models.TextField(max_length=300)
    criado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.conteudo
        