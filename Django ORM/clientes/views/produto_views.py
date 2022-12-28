from django.http import HttpResponse
from ..forms.produto_forms import ProdutoForm
from django.shortcuts import render, redirect
from ..services import produtos_service
from ..entidades.produto import Produto

def inserir_produto(request):
    if request.method == 'POST':
        produto = ProdutoForm(request.POST)
        if produto.is_valid():
            nome = produto.cleaned_data['nome']
            descricao = produto.cleaned_data['descricao']
            valor = produto.cleaned_data['valor']
            produto_novo = Produto(
                nome = nome,
                descricao = descricao,
                valor = valor
            )
            produtos_service.inserir_produto(produto_novo)
            return HttpResponse('SUCCESS')
    else:
        form_produto = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {'form_produto': form_produto})

def listar_produtos(request):
    produtos = produtos_service.listar_produto()
    return render(request, 'produtos/lista_produtos.html', {'produtos':produtos})