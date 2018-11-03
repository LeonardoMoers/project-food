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
    url(r'^usuario/', my_views.CadastroUsuario.as_view(), name='usuario'),
    url(r'^editar_usuario/(?P<usuario_id>\d+)/$', my_views.CadastroUsuario.as_view()),

    url(r'^cadastro_estabelecimento/$', my_views.add_estabelecimento, name='cadastroEstabelecimento'),
    

]



