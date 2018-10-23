from django.db import models

class Categoria(models.Model):
    categoria_produto = models.CharField(max_length=100, blank=False, null=False)
