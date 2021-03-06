from django.db import models
from .subCategoria import SubCategoria
from .estabelecimento import Estabelecimento
from .categoria import Categoria

class Produto(models.Model):
    categoria_idCategoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subCategoria_idsubCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    estabelecimento_idestabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=100)
    descricao_produto = models.CharField(max_length=100)
    adicionais_produto = models.CharField(max_length=100, blank=True, null=True)
    imagem_produto = models.ImageField(upload_to="images/produto")

    objetos = models.Manager()

    def __str__(self):
        return self.nome_produto

