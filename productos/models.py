from django.db import models


#campos para relaciones
#OneToOneField -> uno a uno
#ForeignKey -> uno a muchos
#ManyToManyField -> muchos a muchos

class Detalles_producto(models.Model):
    descripcion = models.TextField(max_length=500)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

from categorias.models import Categoria
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    def _str_(self):
        return self.nombre
