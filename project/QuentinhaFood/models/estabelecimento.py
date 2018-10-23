from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Estabelecimento(models.Model):
	nome_usuario = models.ForeignKey('usuario.User', on_delete=models.CASCADE)
	razao_social = models.CharField(max_length=100)
	cnpj = models.IntegerField(validators=[validate_phone])
	telefone_estabelecimento = models.IntegerField(validators=[validate_phone])
	telefoneAlternativo_estabelecimento = models.IntegerField(validators=[validate_phone])
	email_estabelecimento = models.EmailField()
	site_estabelecimento = models.CharField()
	facebook_estabelecimento = models.CharField()
	twitter_estabelecimento = models.CharField()
	instagram_estabelecimento = models.CharField()
	imagem_estabelecimento = models.ImageField()

def validate_phone(value):
	aux = str(value)
	if len(aux) < 8 or len(aux) > 11:
		raise ValidationError(
			_('%(value)s is not valid, please follow example: (xx) 9 XXXX-XXXX or XXXX-XXXX'),
			params={'value': value}
		)