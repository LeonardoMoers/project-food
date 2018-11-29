from django.contrib import admin

from QuentinhaFood.models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'first_name',)

admin.site.register(Usuario, UsuarioAdmin),
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Estabelecimento)
admin.site.register(Categoria)
admin.site.register(Estado)
admin.site.register(Produto)
admin.site.register(SubCategoria)
