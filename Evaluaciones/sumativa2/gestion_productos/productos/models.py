from django.db import models

# Modelo Marca
class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Característica
class Caracteristica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Producto
class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Asegúrate de que este campo exista
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)  # Valor por defecto
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    caracteristicas = models.ManyToManyField(Caracteristica)

    def __str__(self):
        return self.nombre
