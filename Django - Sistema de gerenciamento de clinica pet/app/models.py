from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from django.contrib.auth.models import AbstractUser

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=30, blank=False, null=False)
    estado = models.CharField(max_length=2, 
                            choices=STATE_CHOICES, 
                            blank=False, null=False)


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    profissao = models.CharField(max_length=255, blank=False, null=False)


class Pet(models.Model):
    ESPECIE_PET_CHOICES = (
        ('Ca', 'Cachorro'),
        ('Ga', 'Gato'),
        ('Co', 'Coelho'),
    )
    COR_PET_CHOICES = (
        ('Pr', 'Preto'),
        ('Br', 'Branco'),
        ('Ci', 'Cinza'),
        ('Ma', 'Marron'),
        ('Am', 'Amarelo'),
    )
    nome = models.CharField(max_length=50, blank=False, null=False)
    nascimento = models.DateTimeField(null=False, blank=False)
    especie = models.CharField(max_length=2,choices = ESPECIE_PET_CHOICES, blank=False, null=False)
    cor = models.CharField(max_length=2,choices = COR_PET_CHOICES, blank=False, null=False)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)

class ConsultaPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    motivo_consulta = models.CharField(max_length=200, null=False, blank=False)
    peso_atual = models.FloatField(null=False, blank=False)
    medicamento_atual = models.TextField(null=False, blank=True)
    medicamentos_prescritos = models.TextField(null=False, blank=True)
    exames_prescritos = models.TextField(null=False, blank=True)

class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, 'Veterinario'),
        (2, 'Financeiro'),
        (3, 'Atendimento'),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False)