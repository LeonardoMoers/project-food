from django import forms
from ..models import Produto, SubCategoria, Categoria

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ('categoria_idCategoria', 'subCategoria_idsubCategoria', 'nome_produto', 'descricao_produto', 'adicionais_produto', 'imagem_produto')