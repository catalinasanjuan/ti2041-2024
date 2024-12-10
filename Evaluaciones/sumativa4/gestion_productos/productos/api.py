from ninja import NinjaAPI
from .models import Producto

api = NinjaAPI()

@api.get("/productos")
def listar_productos(request):
    productos = Producto.objects.all().values()
    return list(productos)

@api.post("/productos")
def crear_producto(request, nombre: str, precio: float):
    producto = Producto.objects.create(nombre=nombre, precio=precio)
    return {"id": producto.id, "nombre": producto.nombre}

@api.get("/productos/{producto_id}")
def obtener_producto(request, producto_id: int):
    producto = Producto.objects.filter(id=producto_id).values().first()
    return producto
