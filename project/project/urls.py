from django.contrib import admin
from django.urls import path

from django.urls import reverse
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import activate
from django.conf.urls.static import static

from QuentinhaFood import views as my_views

# python manage.py makemigrations

# python manage.py migrate --run-syncdb

urlpatterns = i18n_patterns(
    url(r'^$', my_views.listaEstabelecimentos, name='index'),
    url(r'admin/', admin.site.urls),
    url(r'^usuario/$', my_views.CadastroUsuario.as_view(), name='usuario'),
    url(r'^editar/(?P<user_id>\w+)/$', my_views.CadastroUsuario.as_view(), name='update_usuario'),
    url(r'^perfil/$', my_views.perfilUsuario, name='perfil_usuario'),

    url(r'^entrar/$', auth_views.LoginView.as_view(
        template_name='usuario/login.html'),
        name='login'),

    url(r'^sair/$', auth_views.LogoutView.as_view(
        next_page='listaEstabelecimentos'),
        name='logout'),


    url(r'^cadastro_produto/$', my_views.add_produto, name='cadastroProduto'),
    url(r'^cadastro_estabelecimento/$', my_views.add_estabelecimento,
        name='cadastroEstabelecimento'),
    url(r'^lista_estabelecimento/$', my_views.listaEstabelecimentos,
        name='listaEstabelecimentos'),

    url(r'^lista_estabelecimento/(?P<pk>\w+)/$', my_views.listaProdutos, name='listaProdutos'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)