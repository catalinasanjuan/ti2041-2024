from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para listar productos
    path('registro/', views.registro_producto, name='registro'),
    path('resultado/<int:producto_id>/', views.resultado, name='resultado'),
]
