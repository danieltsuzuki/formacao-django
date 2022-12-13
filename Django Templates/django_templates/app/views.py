from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    info = {
        'title': 'TEMPLATES DJANGO',
        'principal': 'APRENDENDO SOBRE TEMPLATES DJANGO',
        'num': 5,
    }

    esportes = {
        # '1': {'nome': 'futebol'},
        # '2': {'nome': 'basquete'},
        # '3': {'nome': 'handball'},
    }

    pessoas = {
        '1': {'nome': 'daniel'},
        '2': {'nome':'sarah'},
        '3': {'nome':'adrielly'},
    }

    return render(request, 'index.html', {'info': info, 'esportes': esportes, 'pessoas': pessoas})

def aprender(request):
    return HttpResponse('Você está aprendendo Django')

def numero(request, num):
    return HttpResponse(f'Número {num}')