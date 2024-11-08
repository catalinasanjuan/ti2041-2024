from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Producto,Categoria, Marca
from .forms import ProductoForm

def is_admin_products(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists()

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            request.session['username'] = user.username
            request.session['login_time'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            request.session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()
            
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
    
    # Pasar los datos de sesión al contexto
    context = {
        'productos': productos,
        'username': request.session.get('username'),
        'login_time': request.session.get('login_time')
    }
    
    return render(request, 'index.html', context)

@user_passes_test(is_admin_products)
def registro_producto(request):
    categorias = Categoria.objects.all()  # Obteniendo todas las categorías
    marcas = Marca.objects.all()          # Obteniendo todas las marcas

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a una página de éxito o a la lista de productos, por ejemplo
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
@user_passes_test(is_admin_products)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

@login_required
@user_passes_test(is_admin_products)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})

