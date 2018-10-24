from django.db import models
from .cidade import Cidade
from .usuario import Usuario

class Endereco(models.Model):
    cidade_idcidade=models.ForeignKey(Cidade, on_delete=models.CASCADE, blank=False, null=False)
    usuario_idusuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False)
    rua_endereco=models.CharField(max_length=200, blank=False, null=False)
    numero_endereco=models.IntegerField(blank=False, null=False)
    complemento_endereco=models.CharField(max_length=200)