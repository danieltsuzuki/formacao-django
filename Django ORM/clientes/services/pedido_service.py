from ..models import Pedido
from django.shortcuts import get_object_or_404
from . import produtos_service
from ..models import Produto

def cadastrar_pedido(pedido):
    pedido_bd = Pedido.objects.create(
        cliente = pedido.cliente,
        data_pedido = pedido.data_pedido,
        valor = pedido.valor,
        observacoes = pedido.observacoes,
        status = pedido.status
    )
    pedido_bd.save()
    preco = 0
    for i in pedido.produtos:
        produto = produtos_service.listar_produto_id(i.id)
        pedido_bd.produtos.add(produto)
        # preco += produto.valor
        # pedido_bd.valor.set(preco)

def listar_pedidos():
    return Pedido.objects.select_related('cliente').all()

def listar_pedido_id(id):
    pedido = get_object_or_404(Pedido, pk = id)
    return pedido

def editar_pedido(pedido_antigo, pedido_novo):
    pedido_antigo.cliente = pedido_novo.cliente
    pedido_antigo.data_pedido = pedido_novo.data_pedido
    pedido_antigo.valor = pedido_novo.valor
    pedido_antigo.observacoes = pedido_novo.observacoes
    pedido_antigo.status = pedido_novo.status
    pedido_antigo.produtos.set(pedido_novo.produtos)
    pedido_antigo.save(force_update=True)