from django import template

register = template.Library() #cria uma nova templatetag

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs = {'class': arg})