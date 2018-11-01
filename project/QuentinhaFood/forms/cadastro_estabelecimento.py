from django import forms
from .models import estabelecimento

class EstabelecimentoForm(forms.ModelForm):
    nome_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100, validators=[validate_phone])
    telefone_estabelecimento = models.CharField(max_length=100, validators=[validate_phone])
    telefoneAlternativo_estabelecimento = models.CharField(max_length=100, validators=[validate_phone], blank=True,null=True)
    email_estabelecimento = models.EmailField()
    site_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
    facebook_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
    twitter_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
    instagram_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
    imagem_estabelecimento = models.ImageField()

    class Meta:
        model = estabelecimento
        fields = ('nome_usuario','razao_social','cnpj','telefone_estabelecimento','telefoneAlteranativo_estabelecimento','email_estabelecimento','site_estabelecimento','facebook_estabelecimento','twitter_estabelecimento','instagram_estabelecimento','imagem_estabelecimento')

