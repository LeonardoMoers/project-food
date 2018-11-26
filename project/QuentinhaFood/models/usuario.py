from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_cpf(value):
	if len(value) != 11:
		raise ValidationError(
			_('%(value)s não é válido'),
			params={'value': value}
		)
	return True
	

def validate_phone(value):
	if len(value) < 8 or len(value) > 11:
		raise ValidationError(
			_('%(value)s não é válido, ppor favor siga o exemplo: (xx) 9 XXXX-XXXX or XXXX-XXXX'),
			params={'value': value}
		)
	return True

class Usuario(User):
	cpf = models.CharField(max_length=100 ,validators=[validate_cpf])
	telefone_usuario = models.CharField(max_length=100, validators=[validate_phone])
	telefoneAlternativo_usuario = models.CharField(max_length=100, validators=[validate_phone], blank=True, null=True)
	imagem_usuario = models.ImageField(upload_to="images/usuario")
	objetos = models.Manager()
	