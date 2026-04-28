from django.shortcuts import render
from .models import Producto
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg,Count
from django.db.models.functions import TruncMonth

# Create your views here.
#vista de inicio del app 
def index(request):
    return render(request,'inventory/index.html')

# vista para visualizar los producto

class ProductoListView(LoginRequiredMixin,generic.ListView):
    model = Producto
    template_name = 'inventory/producto_list.html'
    
    
# vista para crear
class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    fields = '__all__'
    initial={'stock':0,}
    template_name = 'inventory/producto_form.html'
    success_url = reverse_lazy('inventory:producto_view')
    
# vista para actualizar o editar

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    model = Producto
    fields = ['stock','precio',]
    template_name = 'inventory/producto_update.html'
    success_url = reverse_lazy('inventory:producto_view')
# vista para eliminar

class ProductoDeleteView(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name = 'inventory/producto_delete.html'
    success_url = reverse_lazy('inventory:producto_view')
    
#vista para dashboard
@login_required
def dashboard(request):
    total_producto = Producto.objects.count()
    stock_menor = Producto.objects.filter(stock__lt=5).count()
    stock_medio = Producto.objects.filter(stock__gte=5, stock__lt=20).count()
    stock_alto = Producto.objects.filter(stock__gt=20).count()
    promedio_precio = Producto.objects.aggregate(promedio=Avg('precio'))['promedio']
    ultimo_5_producto = Producto.objects.order_by('fecha_creacion')[:5]
    agregado_mes=( Producto.objects.annotate(mes_a= TruncMonth('fecha_creacion'))
    .values('mes_a')
    .annotate(cantidad=Count('id'))
    .order_by('mes_a')
    )
    contexto={
        'total_producto':total_producto,
        'stock_menor':stock_menor,
        'stock_medio':stock_medio,
        'stock_alto':stock_alto,
        'promedio_precio':promedio_precio,
        'ultimo_5_productos':ultimo_5_producto,
        'agregado_mes' : agregado_mes
        
    }
    return render(request,'inventory/dashboard.html',contexto)
