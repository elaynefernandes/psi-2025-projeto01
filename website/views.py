from django.shortcuts import render


novidades = [
        {
            'titulo': 'Boneca Moranguinho Novabrink',
            'conteudo': 'Chegou aí uma super novidade para as crianças que amam Moranguinho: A boneca da Moranguinho da série Moranguinho na Grande Cidade é o mais novo lançamento da Novabrink para o Natal.',
            "imagem": "website/img/n1.png",
            'link': 'https://www.ciatoy.com.br/boneca---moranguinho--1780--novabrink/p'
        },
        {
            'titulo': 'Produtos Moranguinho Água de Cheiro',
            'conteudo': 'Resgatando a memória afetiva dos consumidores, a Água de Cheiro lança uma linha edição limitada de hidratantes corporais e body splash da Moranguinho Vintage.',
            'imagem': "website/img/n2.png",
            'link': 'https://www.aguadecheiro.com.br/busca'
        },
        {
            'titulo': 'Moranguinho na Cidade Grande está disponível no Prime Vídeo',
            'conteudo': 'Confira os desafios culinários de Moranguinho na Cidade Grande com suas amigas Laranjinha, Lima Limão, Gotinha de Limão, Amora Linda e claro sua fiel companheira a Pudim.',
            'imagem': "website/img/n3.png",
            'link': 'https://www.primevideo.com/detail/Moranguinho/0LY2WQHPMV3K907CKWFAIU0TV7'
        }]


def index(request): 
    context = {
        "novidades":novidades
    }
    return render(request, "website/index.html", context)

secao1 = {
    'titulo': 'Quem é Moranguinho?',
    'conteudo': 'Moranguinho é uma personagem infantil criada nos Estados Unidos em 1977. Ela é conhecida por seu visual fofo, com um chapéu de morango e roupas coloridas. Vive em um lugar mágico chamado Jardim de Morango e adora fazer bolos, cuidar dos amigos e espalhar alegria por onde passa. A Moranguinho se tornou um símbolo de doçura, amizade e imaginação para várias gerações de crianças.',
    'imagem': 'website/img/img1.jpg'
}

secao2 = {
    'titulo': 'O que ela ensina?',
    'conteudo': 'A Moranguinho ensina valores importantes como a amizade, o respeito, a gentileza e o trabalho em equipe. Com suas atitudes no dia a dia, ela mostra como é importante ajudar os outros, cuidar da natureza e nunca desistir diante das dificuldades. Suas histórias inspiram as crianças a serem mais doces, responsáveis e solidárias.',
    'imagem': 'website/img/img2.jpg'
}

secao3 = {
    'titulo': 'Onde ela vive',
    'conteudo': 'Moranguinho vive em um lugar encantado chamado Jardim de Morango. É um mundo colorido, cheio de flores, frutas e aromas deliciosos. Lá, tudo é alegre e mágico — as casas são feitas de doces, as árvores dão frutas o ano todo e os amigos vivem sempre perto. É nesse cantinho especial que Moranguinho cuida da natureza, prepara receitas deliciosas e compartilha momentos felizes com seus companheiros.',
    'imagem': 'website/img/casa.jpg'
}

def sobre(request): 
    context = {
        "secao1" : secao1,
        "secao2" : secao2,
        "secao3" : secao3
    }
    return render(request, "website/sobre.html", context)

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

postagens = [
        {
            'titulo': '🌸 Um dia no campo',
            'conteudo': 'Hoje foi um dia maravilhoso! Eu e minhas amigas fomos colher morangos no campo. O sol estava brilhando e o vento cheirava a flores fresquinhas! 🍓🌞',
            'data': '09 de Julho de 2025',
        },
        {
            'titulo': '🎂 Aniversário da Framboesinha',
            'conteudo': 'Fizemos uma festa surpresa para a Framboesinha. Tinha bolo de frutas, decoração rosa e muitas risadas. Ela adorou tudo!',
            'data': '07 de Julho de 2025',
        },
        {
            'titulo': '☔ Dia chuvoso',
            'conteudo': 'Hoje choveu bastante, então ficamos em casa fazendo cupcakes e brincando de tabuleiro. Às vezes, os dias simples são os mais doces!',
            'data': '05 de Julho de 2025',
        }]

atividades = [
        {
            'titulo': 'Moranguinho e amigas',
            'conteudo': 'Vamos colorir suas personagens favoritas!',
            "imagem": "website/img/amigas.jpg",
            'atividade': 'website/media/amigas.pdf'
        },
        {
            'titulo': 'Moranguinho',
            'conteudo': 'Adicione cores nesta folha de colorir da Amora Linda e Cheesecake',
            "imagem": "website/img/m.jpg",
            'atividade': 'website/media/moranguinhoo.pdf'
}]

def diario(request): 
    context ={
        "postagens": postagens, 
        "atividades": atividades
    }
    return render(request, "website/diario.html", context)
     
