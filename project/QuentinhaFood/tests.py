from django.test import TestCase
from ..models import Usuario
from django.test.client import Client

class Usuario_teste(TestCase):
	
	def test_login(self):
		c = Client()
		response = c.post('/login/', {'username': 'john', 'password': 'smith'})
		response.status_code
		response = c.get('/customer/details/')
		response.content
	
	def test_cpf(self):
		cpf = Usuario
		self.assertEquals(cpf.validate_cpf('12345678910')
		self.assertEquals(cpf.validate_cpf('123456789101112', ValidationErr())
	
	def test_telefone(self):
		fone = Usuario
		self.assertEquals(fone.validate_phone('12345678')
		self.assertEquals(fone.validate_phone('1234567891011', ValidationErr())
		
