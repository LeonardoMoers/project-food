from django.shortcuts import render
from ..forms.cadastro_produto import ProdutoForm
from ..models.usuario import Usuario
from ..models.subCategoria import SubCategoria
from ..models.estabelecimento import Estabelecimento
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

@login_required
def add_produto(request):
    template = 'produto/cadastro_produto.html'
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            user = Usuario.objects.get(username=request.user)
            estabelecimento = Estabelecimento.objetos.get(nome_usuario=user)
            produto.estabelecimento_idestabelecimento = estabelecimento
            produto.save()
        else:
            print(form.errors)
    else:
        form = ProdutoForm()

    context_dict = {'form': form}
    return render(request, template, context_dict)

def returnSubCategoria(request):
    data =  SubCategoria.objetos.get(categoria_idcategoria=request)
    obj = serializers.serialize('json', data)
    return HttpResponse(obj, content_type='application/json')