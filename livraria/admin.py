from django.contrib import admin

from .models import Autor, Categoria, Compra, Editora, Livro, ItensCompra

admin.site.register(Autor)

admin.site.register(Categoria)

admin.site.register(Compra)

admin.site.register(Editora)

admin.site.register(Livro)

admin.site.register(ItensCompra)



