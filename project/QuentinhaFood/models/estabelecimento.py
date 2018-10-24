from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .usuario import Usuario

def validate_phone(value):
	aux = str(value)
	if len(aux) < 8 or len(aux) > 11:
		raise ValidationError(
			_('%(value)s is not valid, please follow example: (xx) 9 XXXX-XXXX or XXXX-XXXX'),
			params={'value': value}
		)

class Estabelecimento(models.Model):
	nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False)
	razao_social = models.CharField(max_length=100, blank=False, null=False)
	cnpj = models.IntegerField(validators=[validate_phone], blank=False, null=False)
	telefone_estabelecimento = models.IntegerField(validators=[validate_phone], blank=False, null=False)
	telefoneAlternativo_estabelecimento = models.IntegerField(validators=[validate_phone])
	email_estabelecimento = models.EmailField(blank=False, null=False)
	site_estabelecimento = models.CharField(max_length=200)
	facebook_estabelecimento = models.CharField(max_length=200)
	twitter_estabelecimento = models.CharField(max_length=200)
	instagram_estabelecimento = models.CharField(max_length=200)
	imagem_estabelecimento = models.ImageField(blank=False, null=False)