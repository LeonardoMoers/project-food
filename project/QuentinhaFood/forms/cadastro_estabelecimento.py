from django import forms
from ..models import Estabelecimento

class EstabelecimentoForm(forms.ModelForm):
    #nome_usuario = forms.CharField(max_length=100)
    razao_social = forms.CharField(max_length=100)
    cnpj = forms.CharField(max_length=100)
    telefone_estabelecimento = forms.CharField(max_length=100)
    telefone_alternativo = forms.CharField(max_length=100)
    email_estabelecimento = forms.EmailField(max_length=100)
    site = forms.CharField(max_length=200)
    facebook = forms.CharField(max_length=200)
    twitter = forms.CharField(max_length=200)
    instagram = forms.CharField(max_length=200)
  #  imagem_estabelecimento = forms.ImageField()

    class Meta:
        model = Estabelecimento
        fields = ('nome_usuario','razao_social','cnpj','telefone_estabelecimento','telefone_alternativo','email_estabelecimento','site','facebook','twitter','instagram',)

