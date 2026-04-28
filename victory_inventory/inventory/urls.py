from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'inventory'
urlpatterns = [
    path('',views.index ,name='inicio'),
    path('producto/',views.ProductoListView.as_view(),name='producto_view'),   
    path('crear/',views.ProductoCreateView.as_view(),name='producto_crear'),   
    path('producto/<int:pk>update/',views.ProductoUpdateView.as_view(),name='producto_update'),   
    path('producto/<int:pk>delete/',views.ProductoDeleteView.as_view(),name='producto_delete'),   
    path('dashboard/',views.dashboard,name='dashboard'),   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)