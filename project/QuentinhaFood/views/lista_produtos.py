from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.produto import Produto
from ..models.estabelecimento import Estabelecimento


@login_required
def listaProdutos(request, nomeEstabelecimento):
    template_name = "estabelecimento/pagina_estabelecimento.html"
    estabelecimento = Estabelecimento.objetos.get(razao_social=nomeEstabelecimento)
    produtos = Produto.objetos.all().filter(estabelecimento_idestabelecimento=estabelecimento)
  
    if produtos is None:
        context_dict = {'estabelecimento': estabelecimento}
    else:
        context_dict = {'estabelecimento': estabelecimento, 'produtos': produtos}
    
    return render(request, template_name, context_dict)