from django.db import models
from .subCategoria import SubCategoria
from .estabelecimento import Estabelecimento

class Produto(models.Model):
    subCategoria_idsubCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    estabelecimento_idestabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=100)
    descricao_produto = models.CharField(max_length=100)
    adicionais_produto = models.CharField(max_length=100, blank=True, null=True)
    imagem_produto = models.ImageField(upload_to="images/produto")

    def __str__(self):
        return self.nome_produto

