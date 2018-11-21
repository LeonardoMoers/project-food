from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..forms.usuario import UserForm, UpdateUser
from ..models.usuario import Usuario
from django.contrib.auth import authenticate, login

def cadastroUser(request):
    template = 'usuario/cadastro.html'
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/lista_estabelecimento/')
        else:
            print(form.errors)
    else:
        form = UserForm()

    context_dict = {'form': form}
    return render(request, template, context_dict)

def updateUser(request, id):
    template = 'usuario/update_usuario.html'
    if request.method == 'POST':
        #form = UserForm(data=request.POST, files=request.FILES, instance = Usuario.objects.get(id=id))
        Usuario.objects.filter(id=id).update(**request.POST)        
    else:
        form = UserForm(instance = Usuario.objects.get(id=id))
        
    context_dict = {'form': form}
    return render(request, template, context_dict)
    