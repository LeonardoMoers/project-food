from django.shortcuts import render
from ..forms.usuario import UserForm, UpdateUser
from ..models.usuario import Usuario
from django.contrib.auth import authenticate, login
from django.views.generic.base import View


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

    def post(self, request):
        if request.method == 'POST':
            user_id = request.POST['user_id']

            if user_id:
                userObj = Usuario.objects.get(id=user_id)
                form = UpdateUser(instance=userObj, data=request.POST)
            else:
                form = UserForm(request.POST, request.FILES)

            if form.is_valid():
                user = form.save()
                msg = "Seus dados foram atualizados!"

                if 'imagem_usuario' in request.FILES:
                    user.imagem_usuario = request.FILES['imagem_usuario']

                user.save()

                return render(request, self.template_name, {'form': form, 'msg': msg})
            else:
                form = UserForm()
                msg = "Ocorreu um erro!"
                return render(request, self.template_name, {'form': form, 'msg': msg})
        else:
            form = UserForm()
            return render(request, self.template_name, {'form': form, 'msg': msg})
