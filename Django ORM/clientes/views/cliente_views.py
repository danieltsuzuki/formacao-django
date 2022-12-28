from django.shortcuts import render, redirect
from ..models import Cliente
from django.http import HttpResponse
from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service

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
            form_cliente = ClienteForm(request.POST)
            form_endereco = EnderecoForm(request.POST)
            #verifica se os dados enviados são válidos, seguindo o padrão 
            #do model e do formulario de cliente
            if form_cliente.is_valid():
                #form.save()
                nome = form_cliente.cleaned_data['nome'] #pega os dados passados no formulario no campo nome
                sexo = form_cliente.cleaned_data['sexo']
                data_nascimento = form_cliente.cleaned_data['data_nascimento']
                email = form_cliente.cleaned_data['email']
                profissao = form_cliente.cleaned_data['profissao']
                if form_endereco.is_valid():
                    rua = form_endereco.cleaned_data['rua']
                    numero = form_endereco.cleaned_data['numero']
                    complemento = form_endereco.cleaned_data['complemento']
                    bairro = form_endereco.cleaned_data['bairro']
                    cidade = form_endereco.cleaned_data['cidade']
                    pais = form_endereco.cleaned_data['pais']
                    endereco_novo = endereco.Endereco(
                        rua = rua,
                        numero = numero,
                        complemento = complemento,
                        bairro = bairro,
                        cidade = cidade,
                        pais = pais
                    )
                    endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                    cliente_novo = cliente.Cliente(
                            nome=nome, 
                            sexo=sexo, 
                            email=email, 
                            profissao=profissao, 
                            data_nascimento=data_nascimento,
                            endereco = endereco_bd
                    )
                    cliente_service.cadastrar_cliente(cliente_novo)
                    return redirect('listar_clientes')
        else:
            form_cliente = ClienteForm()
            form_endereco = EnderecoForm()
        return render(request, 'clientes/form_cliente.html', {'form_cliente':form_cliente, 'form_endereco':form_endereco})
    
def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/listar_cliente.html', {'cliente': cliente})

def editar_cliente(request, id):
    cliente_antigo = cliente_service.listar_cliente_id(id)
    if cliente_antigo.endereco == None:
        form_endereco = EnderecoForm(request.POST or None)
    else:
        endereco_antigo = endereco_service.listar_endereco_id(cliente_antigo.endereco.id)
        form_endereco = EnderecoForm(request.POST or None, instance = endereco_antigo)
    form_cliente = ClienteForm(request.POST or None, instance = cliente_antigo)
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data['nome'] #pega os dados passados no form_clienteulario no campo nome
        sexo = form_cliente.cleaned_data['sexo']
        data_nascimento = form_cliente.cleaned_data['data_nascimento']
        email = form_cliente.cleaned_data['email']
        profissao = form_cliente.cleaned_data['profissao']
        
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data['rua']
            numero = form_endereco.cleaned_data['numero']
            complemento = form_endereco.cleaned_data['complemento']
            bairro = form_endereco.cleaned_data['bairro']
            cidade = form_endereco.cleaned_data['cidade']
            pais = form_endereco.cleaned_data['pais']

            endereco_novo = endereco.Endereco(
                rua = rua,
                numero = numero,
                complemento = complemento,
                bairro = bairro,
                cidade = cidade,
                pais = pais
            )

            if cliente_antigo.endereco == None:
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(
                    nome=nome, 
                    sexo=sexo, 
                    email=email, 
                    profissao=profissao, 
                    data_nascimento=data_nascimento,
                    endereco = endereco_bd
                    )
            else:
                endereco_service.editar_endereco(endereco_antigo, endereco_novo)
                cliente_novo = cliente.Cliente(
                        nome=nome, 
                        sexo=sexo, 
                        email=email, 
                        profissao=profissao, 
                        data_nascimento=data_nascimento,
                        endereco = cliente_antigo.endereco.id
                        )

            cliente_service.editar_cliente(cliente_antigo, cliente_novo)
            return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})

def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    endereco = endereco_service.listar_endereco_id(cliente.endereco.id)
    if request.method == 'GET':
        return render(request, 'clientes/confirmar_exclusao.html', {'cliente': cliente})
    cliente_service.remover_cliente(cliente)
    endereco_service.remover_endereco(endereco)
    return redirect('listar_clientes')

