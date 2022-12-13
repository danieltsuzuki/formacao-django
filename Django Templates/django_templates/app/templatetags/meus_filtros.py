from django import template

register = template.Library()

@register.filter(name='remover_letra')
def remover_letra(variavel, caracter):
    return variavel.replace(caracter, '')