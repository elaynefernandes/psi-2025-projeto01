from django.shortcuts import render
from .models import Novidade, Personagem, Secao, Postagem, Atividade

def index(request):
    novidades = Novidade.objects.all()
    context = {"novidades": novidades}
    return render(request, "website/index.html", context)

def sobre(request):
    secoes = Secao.objects.all()
    context = {"secoes": secoes}
    return render(request, "website/sobre.html", context)

def elenco(request):
    personagens = Personagem.objects.all()
    context = {"personagens": personagens}
    return render(request, "website/elenco.html", context)

def diario(request):
    postagens = Postagem.objects.all()
    atividades = Atividade.objects.all()
    context = {"postagens": postagens, "atividades": atividades}
    return render(request, "website/diario.html",context)