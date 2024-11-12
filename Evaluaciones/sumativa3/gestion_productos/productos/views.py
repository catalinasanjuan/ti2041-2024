from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Producto,Categoria, Marca
from .forms import ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists()

def solo_ver(user):
    return user.groups.filter(name='VIEW_ONLY').exists()


def is_admin_products(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists()

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige en función del grupo del usuario
            if user.groups.filter(name='VIEW_ONLY').exists():
                return redirect('listar_productos')  # Redirige a listar_productos si está en VIEW_ONLY
            else:
                return redirect('index')  # Redirige a index para otros usuarios (admin)
        else:
            messages.error(request, "Credenciales incorrectas. Por favor, intenta nuevamente.")
    return render(request, 'login.html')


@login_required
def index(request):
    productos = Producto.objects.all()
    categoria = request.GET.get('categoria')
    marca = request.GET.get('marca')
    
    if categoria:
        productos = productos.filter(categoria__nombre=categoria)
    if marca:
        productos = productos.filter(marca__nombre=marca)
  
    context = {
        'productos': productos,
        'username': request.session.get('username'),
        'login_time': request.session.get('login_time')
    }
    
    return render(request, 'index.html', context)

@user_passes_test(es_admin)
def registro_producto(request):
    categorias = Categoria.objects.all() 
    marcas = Marca.objects.all()          

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ProductoForm()

    context = {
        'form': form,
        'categorias': categorias,
        'marcas': marcas
    }
    return render(request, 'registro.html', context)

@login_required
def resultado(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'resultado.html', {'producto': producto})

@login_required
@user_passes_test(es_admin)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm(instance=producto)
    

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    
    return render(request, 'editar_producto.html', {
        'form': form,
        'producto': producto,
        'categorias': categorias,
        'marcas': marcas
    })
@login_required
@user_passes_test(es_admin)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='VIEW_ONLY').exists())
def listar_productos(request):
    productos = Producto.objects.all()
    categoria = request.GET.get('categoria')
    marca = request.GET.get('marca')
    
    if categoria:
        productos = productos.filter(categoria__nombre=categoria)
    if marca:
        productos = productos.filter(marca__nombre=marca)
  
    context = {
        'productos': productos
    }
    
    return render(request, 'listar_productos.html', context)
