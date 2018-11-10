from django.shortcuts import render
from ..forms.usuario import UserForm

def cadastroUser(request):
    template = 'usuario/cadastro.html'

    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(form.errors)
    else:
        form = UserForm()

    context_dict = {'form': form}
    return render(request, template, context_dict)            