from django.db import models
from django.utils import timezone

## exemplo a ser trabalhado
## 1 cliente só pode ter 1 endereço
## 1 cliente = 1 endereço

class Endereco(models.Model):
    BAIRRO = (
        ("plano diretor norte", "Planto diretor norte"),
        ("plano diretor sul", "Plano diretor sul"),
        ("taquaralto", "Taquaralto"),
    )
    CIDADE = (
        ("palmas", "Palmas"),
        ("paraiso", "Paraiso"),
        ("araguaina", "Araguaina"),
    )
    PAIS = (
        ("brasil", "Brasil"),
    )

    rua = models.CharField(max_length = 200, blank = False, null = False)
    numero = models.IntegerField(blank = False, null = False)
    complemento = models.CharField(max_length = 200, blank = False, null = False)
    bairro = models.CharField(max_length = 100, choices = BAIRRO, blank = False, null = False)
    cidade = models.CharField(max_length = 100, choices = CIDADE, blank = False, null = False)
    pais = models.CharField(max_length = 100, choices = PAIS, blank = False, null = False)

    def __str__(self):
        return self.rua


class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, blank = False, null = False)
    data_nascimento = models.DateField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    profissao = models.CharField(max_length = 50)
    sexo = models.CharField(max_length = 1, choices = SEXO_CHOICES, null = False, blank = False)
    endereco = models.OneToOneField(Endereco, on_delete = models.SET_NULL, null = True) #SET_NULL se o endereço for deletado, o cliente terá endereço setado como NULL

    def __str__(self):
        return self.nome


# N PEDIDOS N PRODUTOS

class Produto(models.Model):
    nome = models.CharField(max_length=500, blank=False, null=False)
    descricao = models.CharField(max_length = 100, blank=False, null=False)
    valor = models.FloatField(blank = False, null = False)

    def __str__(self):
        return self.nome

# 1 Cliente N Pedidos

class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )

    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, null = False, blank = False) # CASCADE quando o cliente for deletado, o pedido também será deletado
    data_pedido = models.DateField(default = timezone.now)
    valor = models.FloatField(blank = False, null = False)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES, blank = False, null = False)
    observacoes = models.CharField(max_length = 100, null = True, blank = True)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome

