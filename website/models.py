from django.db import models

class Novidade(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="novidades/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    fruta = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="personagens/", blank=True, null=True)

    def __str__(self):
        return self.nome


class Secao(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="secoes/", blank=True, null=True)

    def __str__(self):
        return self.titulo


class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="atividades/", blank=True, null=True)
    atividade = models.FileField(upload_to="atividades/", blank=True, null=True)

    def __str__(self):
        return self.titulo
