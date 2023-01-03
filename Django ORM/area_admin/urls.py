from django.contrib import admin
from django.urls import path, include
from clientes.views import index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', index_views.index, name='index'),
]
