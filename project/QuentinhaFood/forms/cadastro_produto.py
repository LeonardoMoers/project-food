from django import forms
from ..models import Produto

class ProdutoForm(forms.ModelForm):
   
    class Meta:
        model = Produto
        fields = ('subCategoria_idsubCategoria', 'nome_produto', 'descricao_produto', 'adicionais_produto', 'imagem_produto')