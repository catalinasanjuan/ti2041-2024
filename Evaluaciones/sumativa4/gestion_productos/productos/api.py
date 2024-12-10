from ninja import NinjaAPI
from .models import Producto
from django.contrib.auth.models import User  # Importación necesaria
from rest_framework_simplejwt.tokens import RefreshToken

api = NinjaAPI(title="Gestión de Productos API", version="1.0", description="API para gestionar productos.")

# Obtener lista de productos
@api.get("/productos", tags=["Productos"])
def listar_productos(request):
    productos = Producto.objects.all().values()
    return list(productos)

# Crear un producto
@api.post("/productos", tags=["Productos"])
def crear_producto(request, nombre: str, precio: float):
    producto = Producto.objects.create(nombre=nombre, precio=precio)
    return {"id": producto.id, "nombre": producto.nombre, "precio": producto.precio}

# Obtener un producto por ID
@api.get("/productos/{producto_id}", tags=["Productos"])
def obtener_producto(request, producto_id: int):
    producto = Producto.objects.filter(id=producto_id).values().first()
    if producto:
        return producto
    return {"error": "Producto no encontrado"}, 404

# Actualizar un producto por ID
@api.put("/productos/{producto_id}", tags=["Productos"])
def actualizar_producto(request, producto_id: int, nombre: str = None, precio: float = None):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto:
        if nombre:
            producto.nombre = nombre
        if precio is not None:
            producto.precio = precio
        producto.save()
        return {"id": producto.id, "nombre": producto.nombre, "precio": producto.precio}
    return {"error": "Producto no encontrado"}, 404

# Eliminar un producto por ID
@api.delete("/productos/{producto_id}", tags=["Productos"])
def eliminar_producto(request, producto_id: int):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto:
        producto.delete()
        return {"message": "Producto eliminado exitosamente"}
    return {"error": "Producto no encontrado"}, 404

# Endpoint para obtener un token de acceso
@api.post("/token")
def obtener_token(request, username: str, password: str):
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    return {"error": "Credenciales inválidas"}, 401
