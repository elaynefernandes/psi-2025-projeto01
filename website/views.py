from django.shortcuts import render

def index(request): 
    return render(request, "website/index.html")

def sobre(request): 
    return render(request, "website/sobre.html")

personagens = [
        {
            "nome": "Moranguinho",
            "imagem": "website/img/p1.jpg",
            "descricao": "Líder doce e otimista da turma.",
            "fruta": "Morango 🍓",
            "cor": "Rosa"
        },
        {
            "nome": "Limãozinho",
            "imagem": "website/img/p2.jpg",
            "descricao": "Organizada, inteligente e prática.",
            "fruta": "Limão 🍋",
            "cor": "Verde"
        },
        {
            "nome": "Cerejinha",
            "imagem": "website/img/p3.jpg",
            "descricao": "Animada e cheia de energia.",
            "fruta": "Cereja 🍒",
            "cor": "Vermelho"
        },
        {
            "nome": "Maçãzinha",
            "imagem": "website/img/p4.jpg",
            "descricao": "Amável e carinhosa.",
            "fruta": "Maçã 🍎",
            "cor": "Vermelho claro"
        },
        {
            "nome": "Amora",
            "imagem": "website/img/p5.png",
            "descricao": "Criativa e sonhadora.",
            "fruta": "Amora 🫐",
            "cor": "Roxo"
        },
        {
            "nome": "Laranjinha",
            "imagem": "website/img/p6.jpg",
            "descricao": "Cheia de energia e espírito esportivo.",
            "fruta": "Laranja 🍊",
            "cor": "Laranja"
        },
        {
            "nome": "Azedinha",
            "imagem": "website/img/p7.jpg",
            "descricao": "Séria, mas muito inteligente.",
            "fruta": "Uva verde",
            "cor": "Verde e Roxo"
        },
        {
            "nome": "Ameixinha",
            "imagem": "website/img/p8.jpg",
            "descricao": "Elegante e muito educada.",
            "fruta": "Ameixa 🍑",
            "cor": "Roxo escuro"
        },
        {
            "nome": "Uvinha",
            "imagem": "website/img/pp9.jpg",
            "descricao": "Meiga, quietinha, mas muito sábia.",
            "fruta": "Uva 🍇",
            "cor": "Lilás"
        },
        {
            "nome": "pupcake",
            "imagem": "website/img/p10.jpg",
            "descricao": "Cachorrinho brincalhão e leal da moranguinho",
            "fruta": "Morango",
            "cor" : "Vermelho"
        },
        {
            "nome": "Custard",
            "imagem": "website/img/p11.png",
            "descricao": "Gatinha fofa, curiosa e esperta",
            "fruta": "Morango",
            "cor": "Verde"
        },
    ]


def elenco(request): 

    context = {
        "personagens":personagens
    }
    return render(request, "website/elenco.html", context)

def diario(request): 
    return render(request, "website/diario.html")

