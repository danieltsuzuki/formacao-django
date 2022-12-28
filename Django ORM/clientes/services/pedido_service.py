from ..models import Pedido
from django.shortcuts import get_object_or_404

def cadastrar_pedido(pedido):
    Pedido.objects.create(
        cliente = pedido.cliente,
        data_pedido = pedido.data_pedido,
        valor = pedido.valor,
        observacoes = pedido.observacoes,
        status = pedido.status
    )

def listar_pedidos():
    return Pedido.objects.all()

def listar_pedido_id(id):
    pedido = get_object_or_404(Pedido, pk = id)
    return pedido

def editar_pedido(pedido_antigo, pedido_novo):
    pedido_antigo.cliente = pedido_novo.cliente
    pedido_antigo.data_pedido = pedido_novo.data_pedido
    pedido_antigo.valor = pedido_novo.valor
    pedido_antigo.observacoes = pedido_novo.observacoes
    pedido_antigo.status = pedido_novo.status
    pedido_antigo.save(force_update=True)