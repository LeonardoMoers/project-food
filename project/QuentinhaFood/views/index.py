from django.shortcuts import render


def index(request):
    urls = [{'titulo': 'Home', 'link': 'index'}, {'titulo': 'lista_estabelecimento', 'link': 'listaEstabelecimentos'}, {'titulo': 'Usuario', 'link': 'usuario'}, {'titulo': 'cadastro_produto', 'link': 'cadastroProduto'}, {'titulo': 'cadastro_estabelecimento', 'link': 'cadastroEstabelecimento'}]
    context_dict = {'urls': urls}
    return render(request, 'index.html', context=context_dict)
