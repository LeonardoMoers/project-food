from django.test import TestCase
from django.core.exceptions import ValidationError
from .models.usuario import validate_cpf, validate_phone
from django.test.client import Client

class Usuario_teste(TestCase):
	
	def test_login(self):
		c = Client()
		response = c.post('/login/', {'username': '@#$', 'password': '23'})
		self.assertEquals(response.status_code, 404)
		print(response.status_code)
		response = c.get('/customer/details/')
		response.content
	
	def test_cpf(self):
		self.assertEquals(validate_cpf('12345678910'), True)
		self.assertEquals(validate_cpf('123456789101112'), False)
	
	def test_telefone(self):
		self.assertEquals(validate_phone('12345678'), True)
		self.assertEquals(validate_phone('1234567891011'), False)
		
