from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from .forms import cadastro_estabelecimento


def add_estabelecimento(request):
    if request.method == 'POST':
        form = cadastro_estabelecimento(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = cadastro_estabelecimento()
    return render(request, 'QuentinhaFood/cadastro_estabelecimento.html', {'form': form})

