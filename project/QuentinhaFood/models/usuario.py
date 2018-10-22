from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translations import ugettext_lazy as _

class User(models.Model):
	nome_usuario = models.CharField(max_length=100)
	cpf = models.IntegerField(validators=[validate_cpf])
	email_usuario = models.EmailField()
	telefone_usuario = models.IntegerField(validators=[validate_phone])
	telefoneAlternativo_usuario = models.IntegerField(validators=[validate_phone])
	apelido_usuario = models.CharField(max_length=100)
	imagem_usuario = models.ImageField()
# se necessário definir o options do ImageField posteriormente;

def validate_cpf(value):
	aux = str(value);
	if len(aux) != 11:
		raise ValidationError(
			_('%(value)s is not valid'),
			params={'value': value}
		)

def validate_phone(value):
	aux = str(value);
	if len(aux) < 8 or len(aux) > 11:
		raise ValidationError(
			_('%(value)s is not valid, please follow example: (xx) 9 XXXX-XXXX or XXXX-XXXX'),
			params={'value': value}
		)