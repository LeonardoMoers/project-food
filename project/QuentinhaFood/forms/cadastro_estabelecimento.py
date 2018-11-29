from django import forms
from ..models import Estabelecimento


class EstabelecimentoForm(forms.ModelForm):

    razao_social = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'razao_social', 'v-model': 'razao_social'}))
    descricao_estabelecimento = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'descricao_estabelecimento', 'v-model': 'descricao_estabelecimento'}))
    cnpj = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'cnpj', 'v-model': 'cnpj', 'v-mask': '["##############"]'}))
    telefone_estabelecimento = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'telefone_estabelecimento', 'v-model': 'telefone_estabelecimento', 'v-mask': '["####-#####"]'}))
    telefoneAlternativo_estabelecimento = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'telefoneAlternativo_estabelecimento', 'v-model': 'telefoneAlternativo_estabelecimento', 'v-mask': '["####-#####"]'}))
    email_estabelecimento = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'email_estabelecimento', 'v-model': 'email_estabelecimento'})) 
    site_estabelecimento = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'site_estabelecimento', 'v-model': 'site_estabelecimento'}))
    facebook_estabelecimento = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'facebook_estabelecimento', 'v-model': 'facebook_estabelecimento'}))
    twitter_estabelecimento = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'twitter_estabelecimento', 'v-model': 'twitter_estabelecimento'}))
    instagram_estabelecimento = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'instagram_estabelecimento', 'v-model': 'instagram_estabelecimento'}))

    class Meta:
        model = Estabelecimento
        fields = ('razao_social', 'descricao_estabelecimento', 'cnpj', 'telefone_estabelecimento', 'telefoneAlternativo_estabelecimento', 'email_estabelecimento', 'site_estabelecimento', 'facebook_estabelecimento', 'twitter_estabelecimento', 'instagram_estabelecimento', 'imagem_estabelecimento')
