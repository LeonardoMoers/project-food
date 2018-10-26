from django.db import models
from .cidade import Cidade
from .usuario import Usuario

class Endereco(models.Model):
    cidade_idcidade=models.ForeignKey(Cidade, on_delete=models.CASCADE)
    usuario_idusuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rua_endereco=models.CharField(max_length=200)
    numero_endereco=models.IntegerField()
    complemento_endereco=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.rua_endereco