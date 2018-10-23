from django.db import models

class Cidade(models.Model):
    estado_idestado = models.ForeignKey('estado.Estado', on_delete=models.CASCADE)