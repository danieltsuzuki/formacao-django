from django.urls import path
from .views import cliente_views, pedido_views, produto_views


urlpatterns = [
    path('listar_clientes', cliente_views.listar_clientes, name='listar_clientes'),
    path('cadastrar_cliente', cliente_views.inserir_cliente, name='cadastrar_cliente'),
    path('listar_cliente/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
    path('cadastrar_pedido', pedido_views.inserir_pedido, name='cadastrar_pedido'),
    path('listar_pedidos', pedido_views.listar_pedidos, name='listar_pedidos'),
    path('listar_pedido/<int:id>', pedido_views.listar_pedido_id, name='listar_pedido_id'),
    path('editar_pedido/<int:id>', pedido_views.editar_pedido, name = 'editar_pedido'),
    path('cadastrar_produto', produto_views.inserir_produto, name='cadastrar_produto'),
    # path('listar_produto/<int:id>', produto_views.)
    path('listar_produtos', produto_views.listar_produtos, name='listar_produtos')
]
