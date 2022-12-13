from ..models import Cliente
from django.shortcuts import get_object_or_404

def cadastrar_cliente(cliente):
    Cliente.objects.create(
        nome = cliente.nome,
        sexo = cliente.sexo,
        data_nascimento = cliente.data_nascimento,
        email = cliente.email,
        profissao = cliente.profissao
    )

def listar_clientes():
    clientes = Cliente.objects.all()
    return clientes

def listar_cliente_id(id):
    cliente = get_object_or_404(Cliente, pk = id)
    return cliente

def remover_cliente(cliente):
    cliente.delete()

def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.sexo = cliente_novo.sexo
    cliente.profissao = cliente_novo.profissao
    cliente.email = cliente_novo.email
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.save(force_update=True)