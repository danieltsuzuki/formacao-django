from ..models import Endereco
from django.shortcuts import get_object_or_404

def cadastrar_endereco(endereco):
    return Endereco.objects.create(
        rua = endereco.rua,
        numero = endereco.numero,
        complemento = endereco.complemento,
        bairro = endereco.bairro,
        cidade = endereco.cidade,
        pais = endereco.pais
    )

def listar_endereco_id(id):
    endereco = get_object_or_404(Endereco, pk=id)
    return endereco

def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.numero = endereco_novo.numero
    endereco_antigo.complemento = endereco_novo.complemento
    endereco_antigo.bairro = endereco_novo.bairro
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.pais = endereco_novo.pais
    endereco_antigo.save(force_update=True)

def remover_endereco(endereco):
    endereco.delete()