from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from ..forms.usuario import UserForm, UpdateUser
from ..models.usuario import Usuario
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.utils.translation import gettext_lazy as _


class CadastroUsuario(View):
    template_name = 'usuario/cadastro.html'

    def get(self, request, user_id=None):
        if user_id:
            userObj = Usuario.objects.get(id=user_id)
            form = UpdateUser(instance=userObj)
            editar = True
        else:
            form = UserForm()
            editar = False
        return render(request, self.template_name, {'form': form, 'editar': editar, 'user_id': user_id})

    def post(self, request, user_id=None):
        if request.method == 'POST':
            user_id = user_id
            
            if user_id:

                userObj = Usuario.objects.get(id=user_id)
                form = UpdateUser(instance=userObj, data=request.POST)
                editar = True

                if form.is_valid():
                    user = form.save()

                    if 'imagem_usuario' in request.FILES:
                        user.imagem_usuario = request.FILES['imagem_usuario']
                        user.save()
                    
                    msg = "Seus dados foram atualizados!"
                    return render(request, self.template_name, {'form': form, 'msg': msg, 'editar': editar, 'user_id': user_id})
                
                else:
                    msg = "Ocorreu um erro!"
                    return render(request, self.template_name, {'form': form, 'msg': msg, 'user_id': user_id, 'editar': editar})
            
            else:
            
                form = UserForm(request.POST, request.FILES)
                
                if form.is_valid():
                    user = form.save()
                    user.set_password(user.password)

                    if 'imagem_usuario' in request.FILES:
                        user.imagem_usuario = request.FILES['imagem_usuario']
                        user.save()
    
                    login(request, user)
                    return HttpResponseRedirect('/lista_estabelecimento/')
            
                else:

                    msg = 'Ocorreu um erro!'
                    return render(request, self.template_name, {'form': form, 'msg': msg})
