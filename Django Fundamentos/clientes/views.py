from django.shortcuts import render, redirect
from .models import Cliente
from django.http import HttpResponse
from .forms import ClienteForm
from .entidades import cliente
from .services import cliente_service

def listar_clientes(request):
    
    clientes = cliente_service.listar_clientes()
    if not clientes:
        return HttpResponse('Não há clientes cadastrado')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})
    
def inserir_cliente(request):
        #Se o método da requisição for POST
        if request.method == 'POST':
            #Criamos uma instancia do Form e passamos as informações da 
            #requisição com request.POST para a variavel form
            form = ClienteForm(request.POST)
            #verifica se os dados enviados são válidos, seguindo o padrão 
            #do model e do formulario de cliente
            if form.is_valid():
                #form.save()
                nome = form.cleaned_data['nome'] #pega os dados passados no formulario no campo nome
                sexo = form.cleaned_data['sexo']
                data_nascimento = form.cleaned_data['data_nascimento']
                email = form.cleaned_data['email']
                profissao = form.cleaned_data['profissao']
                cliente_novo = Cliente(
                        nome=nome, 
                        sexo=sexo, 
                        email=email, 
                        profissao=profissao, 
                        data_nascimento=data_nascimento)
                cliente_service.cadastrar_cliente(cliente_novo)
                return redirect('listar_clientes')
        else:
            form = ClienteForm()
        return render(request, 'clientes/form_cliente.html', {'form':form})
    
def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/listar_cliente.html', {'cliente': cliente})

def editar_cliente(request, id):
    cliente_antigo = cliente_service.listar_cliente_id(id)
    form = ClienteForm(request.POST or None, instance = cliente_antigo)
    if form.is_valid():
        nome = form.cleaned_data['nome'] #pega os dados passados no formulario no campo nome
        sexo = form.cleaned_data['sexo']
        data_nascimento = form.cleaned_data['data_nascimento']
        email = form.cleaned_data['email']
        profissao = form.cleaned_data['profissao']
        cliente_novo = cliente.Cliente(
                nome=nome, 
                sexo=sexo, 
                email=email, 
                profissao=profissao, 
                data_nascimento=data_nascimento
                )
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form': form})

def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    if request.method == 'GET':
        return render(request, 'clientes/confirmar_exclusao.html', {'cliente': cliente})
    cliente_service.remover_cliente(cliente)
    return redirect('listar_clientes')

