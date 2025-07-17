from django.shortcuts import render

def index(request): 
    return render(request, "website/index.html")

def sobre(request): 
    return render(request, "website/sobre.html")

def elenco(request): 
    return render(request, "website/elenco.html")

def diario(request): 
    return render(request, "website/diario.html")

