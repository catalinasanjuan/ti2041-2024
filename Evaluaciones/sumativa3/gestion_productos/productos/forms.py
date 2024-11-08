from django import forms
from .models import Producto, Categoria, Marca

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Seleccione una categoría")
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label="Seleccione una marca")

    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'categoria', 'marca', 'caracteristicas']
