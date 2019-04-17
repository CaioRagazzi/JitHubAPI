from django.db import models


class Pergunta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    tipo = models.IntegerField()

    def __str__(self):
        return self.nome
