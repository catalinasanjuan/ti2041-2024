from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


def index(request):
    productos = Producto.objects.all()

    # Obtener filtros si están presentes en la solicitud
    categoria = request.GET.get('categoria')
    marca = request.GET.get('marca')

    # Aplicar filtros si es necesario
    if categoria:
        productos = productos.filter(categoria__nombre=categoria)
    if marca:
        productos = productos.filter(marca__nombre=marca)

    return render(request, 'index.html', {'productos': productos})

def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()  # Aquí guardas el producto y lo asignas a una variable
            return redirect('resultado', producto_id=producto.id)  # Rediriges usando el ID del producto
    else:
        form = ProductoForm()

    return render(request, 'registro.html', {'form': form})

def resultado(request, producto_id):
    producto = Producto.objects.get(id=producto_id)  # Obtener el producto por su ID
    return render(request, 'resultado.html', {'producto': producto})

