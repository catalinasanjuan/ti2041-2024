from django.shortcuts import render, redirect

# Lista de productos en memoria
productos = []

def registro_producto(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        # Validar campos
        if not codigo or not nombre or not marca or not fecha_vencimiento:
            return render(request, 'registro.html', {'error': 'Todos los campos son obligatorios.'})

        # Almacenar el producto en memoria
        productos.append({
            'codigo': codigo,
            'nombre': nombre,
            'marca': marca,
            'fecha_vencimiento': fecha_vencimiento
        })

        return redirect('resultado')

    return render(request, 'registro.html')


def resultado_producto(request):
    return render(request, 'resultado.html', {'producto': productos[-1]})


def consulta_productos(request):
    return render(request, 'consulta.html', {'productos': productos})

