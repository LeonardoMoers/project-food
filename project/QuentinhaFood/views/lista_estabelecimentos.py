from django.shortcuts import render
from ..models import Estabelecimento
from django.contrib.auth.decorators import login_required

@login_required
def listaEstabelecimentos(request):
    template_path = "estabelecimento/lista_estabelecimentos.html"
    estabelecimentos_list = Estabelecimento.objetos.all()
    context_dict = {'estabelecimentos': estabelecimentos_list}
    return render(request, template_path, context_dict)
