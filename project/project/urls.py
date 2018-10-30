from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from QuentinhaFood.views.usuario import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('usuario/', CadastroUsuario.as_view(), name='usuario'),
    url(r'admin/', admin.site.urls),
    url(r'^usuario/', CadastroUsuario.as_view(), name='usuario'),
    url(r'^editar_usuario/(?P<usuario_id>\d+)/$', CadastroUsuario.as_view()),
]



