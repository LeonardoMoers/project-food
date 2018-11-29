from django.shortcuts import render
from ..models.produto import Produto
from ..models.estabelecimento import Estabelecimento


def listaProdutos(request, pk):
    template_name = "estabelecimento/pagina_estabelecimento.html"
    estabelecimento = Estabelecimento.objetos.get(pk=pk)
    produtos = Produto.objetos.all().filter(estabelecimento_idestabelecimento=estabelecimento)
  
    if produtos is None:
        context_dict = {'estabelecimento': estabelecimento}
    else:
        context_dict = {'estabelecimento': estabelecimento, 'produtos': produtos}
    
    return render(request, template_name, context_dict)