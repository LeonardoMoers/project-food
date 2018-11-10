from django import forms
from ..models import Estabelecimento

class EstabelecimentoForm(forms.ModelForm):

    class Meta:
        model = Estabelecimento
        fields = ('nome_usuario', 'razao_social', 'cnpj', 'telefone_estabelecimento', 'telefoneAlternativo_estabelecimento', 'email_estabelecimento', 'site_estabelecimento', 'facebook_estabelecimento', 'twitter_estabelecimento', 'instagram_estabelecimento', 'imagem_estabelecimento')