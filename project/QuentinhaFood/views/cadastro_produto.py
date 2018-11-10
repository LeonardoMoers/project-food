from django.shortcuts import render
from ..forms.cadastro_produto import ProdutoForm

def add_produto(request):
    template = 'produto/cadastro_produto.html'
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)
    else:
        form = ProdutoForm()

    context_dict = {'form': form}
    return render(request, template, context_dict)
