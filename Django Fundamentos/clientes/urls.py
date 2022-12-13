from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.listar_clientes, name='listar_clientes'),
    path('cadastrar', views.inserir_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>', views.listar_cliente_id, name='listar_cliente_id'),
    path('editar/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('remover/<int:id>', views.remover_cliente, name='remover_cliente'),
    
]
