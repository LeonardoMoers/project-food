from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_cpf(value):
	aux = str(value)
	if len(aux) != 11:
		raise ValidationError(
			_('%(value)s is not valid'),
			params={'value': value}
		)

def validate_phone(value):
	aux = str(value)
	if len(aux) < 8 or len(aux) > 11:
		raise ValidationError(
			_('%(value)s is not valid, please follow example: (xx) 9 XXXX-XXXX or XXXX-XXXX'),
			params={'value': value}
		)

class Usuario(User):
	cpf = models.IntegerField(validators=[validate_cpf], blank=False, null=False)
	email_usuario = models.EmailField(blank=False, null=False)
	telefone_usuario = models.IntegerField(validators=[validate_phone], blank=False, null=False)
	telefoneAlternativo_usuario = models.IntegerField(validators=[validate_phone])
	apelido_usuario = models.CharField(max_length=100)
	imagem_usuario = models.ImageField(blank=False, null=False)