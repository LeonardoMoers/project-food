from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .usuario import Usuario



class Estabelecimento(models.Model):

	def validate_phone(self):
		if len(self) < 8 or len(self) > 11:
			raise ValidationError(
				_('%(value)s is not valid, please follow example: (xx) 9 XXXX-XXXX or XXXX-XXXX'),
				params={'value': self}
			)


	nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	razao_social = models.CharField(max_length=100)
	cnpj = models.CharField(max_length=100, validators=[validate_phone])
	telefone_estabelecimento = models.CharField(max_length=100, validators=[validate_phone])
	telefoneAlternativo_estabelecimento = models.CharField(max_length=100, validators=[validate_phone], blank=True, null=True)
	email_estabelecimento = models.EmailField()
	site_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
	facebook_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
	twitter_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
	instagram_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
#	imagem_estabelecimento = models.ImageField()
	
	objetos = models.Manager()

	def __str__(self):
		return self.razao_social