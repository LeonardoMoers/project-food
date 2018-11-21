from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from QuentinhaFood import views as my_views 


urlpatterns = [
    url(r'^$', my_views.index, name='index'),
    url(r'admin/', admin.site.urls),
    url(r'^usuario/$', my_views.cadastroUser, name='usuario'),
    url(r'^usuario/(?P<id>\w+)', my_views.updateUser, name='update_usuario'),
    url(r'^perfil/$', my_views.perfilUsuario, name='perfil_usuario'),

    url( r'^entrar/$',auth_views.LoginView.as_view(
        template_name='usuario/login.html'), 
        name='login'),

    url( r'^sair/$',auth_views.LogoutView.as_view(
        next_page='listaEstabelecimentos'),
        name='logout'),


    url(r'^cadastro_produto/$', my_views.add_produto, name='cadastroProduto'),
    url(r'^cadastro_estabelecimento/$', my_views.add_estabelecimento, name='cadastroEstabelecimento'),
    url(r'^lista_estabelecimento/$', my_views.listaEstabelecimentos, name='listaEstabelecimentos'),
]




