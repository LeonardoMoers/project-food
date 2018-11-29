from django.db import models

class Estado(models.Model):
    nome_estado = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_estado