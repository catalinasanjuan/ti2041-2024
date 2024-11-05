from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def index(request):
    productos = Producto.objects.all()
    categoria = request.GET.get('categoria')
    marca = request.GET.get('marca')
    if categoria:
        productos = productos.filter(categoria__nombre=categoria)
    if marca:
        productos = productos.filter(marca__nombre=marca)
    return render(request, 'index.html', {'productos': productos})

@login_required
def registro_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('resultado', producto_id=producto.id)
    else:
        form = ProductoForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def resultado(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'resultado.html', {'producto': producto})
