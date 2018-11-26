from django import forms
from ..models import Produto, SubCategoria, Categoria


class ProdutoForm(forms.ModelForm):
    nome_produto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'nome_produto', 'v-model': 'nome_produto'}))
    descricao_produto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'descricao_produto', 'v-model': 'descricao_produto'}))
    adicionais_produto = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'adicionais_produto', 'v-model': 'adicionais_produto'}))

    class Meta:
        model = Produto
        fields = ('categoria_idCategoria', 'subCategoria_idsubCategoria',
                  'nome_produto', 'descricao_produto', 'adicionais_produto', 'imagem_produto')
