from django.db import models

# classe de usuarios.


class Usuarios(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    grupo = models.CharField(max_length=150)
    senha = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
