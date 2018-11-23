from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.usuario import Usuario
from ..models.estabelecimento import Estabelecimento


@login_required
def perfilUsuario(request):
    template_name = "usuario/perfil_usuario.html"
    usuario = Usuario.objetos.get(username=request.user)
    estabelecimento = Estabelecimento.objetos.get(nome_usuario=usuario)
   
    if (estabelecimento):
    	context_dict = {'usuario': usuario , 'estabelecimento': estabelecimento}
    else:
    	context_dict = {'usuario': usuario}
    return render(request, template_name, context_dict)
