from django.db import models
from perguntas.models import Pergunta


class Formulario(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    perguntas = models.ManyToManyField(Pergunta)

    def __str__(self):
        return self.nome
