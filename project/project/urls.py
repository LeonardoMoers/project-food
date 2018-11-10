from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from QuentinhaFood import views as my_views 

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('usuario/', CadastroUsuario.as_view(), name='usuario'),
    url(r'admin/', admin.site.urls),
    url(r'^usuario/', my_views.cadastroUser, name='usuario'),
    url(r'^cadastro_produto/$', my_views.add_produto, name='cadastroProduto'),
    url(r'^cadastro_estabelecimento/$', my_views.add_estabelecimento, name='cadastroEstabelecimento'),
    url(r'^lista_estabelecimento/$', my_views.listaEstabelecimentos, name='listaEstabelecimentos'),

]




