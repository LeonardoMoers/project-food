from django.http import HttpResponseRedirect
from django.shortcuts import render

from ..forms import EstabelecimentoForm


def add_estabelecimento(request):
    template = 'estabelecimento/cadastro_estabelecimento.html'
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/usuario/')
        else:
            print(form.errors)
    else:
        form = EstabelecimentoForm()
    return render(request, template, {'form': form})