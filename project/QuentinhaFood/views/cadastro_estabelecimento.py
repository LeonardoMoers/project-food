from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..models.usuario import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from ..forms import EstabelecimentoForm

@login_required
def add_estabelecimento(request):
    template = 'estabelecimento/cadastro_estabelecimento.html'
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)

        if form.is_valid():
            estabelecimento = form.save(commit=False)
            user = Usuario.objects.get(username=request.user)
            estabelecimento.nome_usuario = user
            estabelecimento.save()

            new_group, create = Group.objects.get_or_create(name='fornecedor')
            new_group.user_set.add(user)

            return HttpResponseRedirect('/lista_estabelecimento/')
        else:
            print(form.errors)
    else:
        form = EstabelecimentoForm()
    return render(request, template, {'form': form})