from django.shortcuts import render
from ..models import Estabelecimento
from django.contrib.auth.decorators import login_required

def listaEstabelecimentos(request):
   
    template_name = "estabelecimento/lista_estabelecimentos.html"
    estabelecimentos_list = Estabelecimento.objetos.all()
    context_dict = {'estabelecimentos': estabelecimentos_list}

    return render(request, template_name, context_dict)
