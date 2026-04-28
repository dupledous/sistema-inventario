from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','precio','stock','imagen',)
    list_filter = ('nombre',)

# Register your models here.
admin.site.register(Producto,ProductoAdmin)
