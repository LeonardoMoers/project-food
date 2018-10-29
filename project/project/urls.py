from django.contrib import admin
from django.urls import path

from QuentinhaFood.views.usuario import CadastroUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', CadastroUsuario.as_view(), name='usuario'),

]



