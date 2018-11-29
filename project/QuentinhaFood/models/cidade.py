from django.db import models
from .estado import Estado

class Cidade(models.Model):
    estado_idestado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome_cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_cidade