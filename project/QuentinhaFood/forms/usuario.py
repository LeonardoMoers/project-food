from django import forms
from ..models import Usuario
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'username', 'v-model': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'validate', 'id': 'password', 'v-model': 'password'}))
    confirmar_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'validate', 'id': 'confirmar_password', 'v-model': 'confirmar_password'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'validate', 'id': 'email', 'v-model': 'email'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'first_name', 'v-model': 'first_name'}))
    cpf = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'cpf', 'v-model': 'cpf', 'v-mask': '["###########"]' })) 
    telefone_usuario = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'telefone_usuario', 'v-model': 'telefone_usuario', 'v-mask': '["####-####"]'}))
    telefoneAlternativo_usuario = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'id': 'telefoneAlternativo_usuario', 'v-model': 'telefoneAlternativo_usuario', 'v-mask': '["####-####"]'}))
    # imagem_usuario = forms.CharField(
    #     attrs={'class': 'validate', 'id': 'imagem_usuario'})

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
                _("Senha e confirmação não coincidem")
            )

class UpdateUser(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = (
            'last_name','last_login', "groups", "user_permissions", "helptext", "is_staff", "date_joined", 'is_active',
            'is_superuser',
            'username', 'password', 'confirmar_password', 'cpf')
