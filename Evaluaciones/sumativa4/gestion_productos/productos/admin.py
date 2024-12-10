from django.contrib import admin
from .models import Producto, Marca, Categoria, Caracteristica  # Importa tus modelos

# Registra los modelos para que aparezcan en el administrador
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Caracteristica)
