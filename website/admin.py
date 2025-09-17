from django.contrib import admin
from .models import Novidade, Personagem, Secao, Postagem, Atividade
# Register your models here.
admin.site.register(Novidade)
admin.site.register(Personagem)
admin.site.register(Secao)
admin.site.register(Postagem)
admin.site.register(Atividade)
