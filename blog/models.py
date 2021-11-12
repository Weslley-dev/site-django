from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): # criando classe do post do site
    title = models.CharField(max_length=255) # o titulo do site tem que receber até 255 caractere
    slug = models.SlugField(max_length=255, unique=True) # o slug fica logo abaixo do titulo, é como se fosse o subtitulo 
    # também é onde fica o url, por exemplo www.meusite.com/blog/introducao-ao-django
    # o unique quer dizer que ele tem que ser unico.
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ele vai guardar o id do usuario do post
    body = models.TextField() # o corpo do post, o texto.
    created = models.DateTimeField(auto_now_add=True) # adiciona a data e hora de quando o artigo foi criado.
    updated = models.DateTimeField(auto_now=True) # a cada modificacao que eu fizer no artigo o update é atualizado
    