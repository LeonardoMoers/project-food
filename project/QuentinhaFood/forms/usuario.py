from django import forms
from ..models import Usuario

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmar_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'confirmar_password', 'email', 'first_name', 'cpf', 'telefone_usuario', 
        'telefoneAlternativo_usuario', 'imagem_usuario')
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")
        if password != confirmar_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
    