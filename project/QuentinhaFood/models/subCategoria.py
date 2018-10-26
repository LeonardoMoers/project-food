from django.db import models
from .categoria import Categoria

class SubCategoria(models.Model):
    categoria_idcategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subCategoria_produto = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.subCategoria_produto