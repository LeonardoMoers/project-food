from django.shortcuts import render
from ..models import Estabelecimento

def listaEstabelecimentos(request):
    template_path = "estabelecimento/lista_estabelecimentos.html"
    estabelecimentos_list = Estabelecimento.objetos.all()
    context_dict = {'estabelecimentos': estabelecimentos_list}
    return render(request, template_path, context_dict)
