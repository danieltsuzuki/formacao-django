from django.shortcuts import get_object_or_404
from ..models import Produto

def inserir_produto(produto):
    Produto.objects.create(
        nome = produto.nome,
        descricao = produto.descricao,
        valor = produto.valor
    )

def listar_produto():
    return Produto.objects.all()

def listar_produto_id(id):
    produto = get_object_or_404(Produto, pk=id)
    return produto