from django import forms
from ..models import Usuario



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ('first_name', 'cpf', 'email', 'telefone_usuario', 
        'telefoneAlternativo_usuario', 'username', 'password')