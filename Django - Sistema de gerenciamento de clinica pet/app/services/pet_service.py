from ..models import Pet

def cadastrar_pet(pet):
   Pet.objects.create(
    nome = pet.nome,
    nascimento = pet.nascimento,
    especie = pet.especie,
    cor = pet.cor,
    dono = pet.dono
   )

def listar_pets(id):
   """Retorna todos os pets de um determinado dono"""
   pets = Pet.objects.filter(dono=id).all()
   return pets

def editar_pet(pet, pet_novo):
   pet.dono = pet_novo.dono
   pet.nome = pet_novo.nome
   pet.nascimento = pet_novo.nascimento
   pet.especie = pet_novo.especie
   pet.cor = pet_novo.cor
   pet.save(force_update=True)

def listar_pet_id(id):
   pet = Pet.objects.get(id=id)
   return pet