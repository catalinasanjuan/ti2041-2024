# productos/apps.py
from django.apps import AppConfig

class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'

    def ready(self):
        import productos.signals  # Conectamos las señales al cargar la aplicación