from django.db import models
from django.urls import reverse

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False, help_text="el nombre del producto")
    descripcion = models.CharField(max_length=200,help_text="la descripcion", null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen= models.ImageField(upload_to="inventory",null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Producto"
    
    def __str__(self):
        return f"{self.nombre}(${self.precio}- stock:{self.stock}) {self.imagen},{self.fecha_creacion}"
    
    def get_absolute_url(self):
        return reverse("inventory:producto_view")
    
    