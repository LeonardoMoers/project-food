from django.db import models
from .subCategoria import SubCategoria
from .estabelecimento import Estabelecimento

class Produto(models.Model):
    subCategoria_idsubCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    estabelecimento_idestabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=100, blank=False, null=False)
    descricao_produto = models.CharField(max_length=100, blank=False, null=False)
    adicionais_produto = models.CharField(max_length=100)
    imagem_produto = models.ImageField(blank=False, null=False)

