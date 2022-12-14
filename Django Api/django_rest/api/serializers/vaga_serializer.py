from rest_framework import serializers
from ..models import Vaga
from rest_framework.reverse import reverse

class VagaSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Vaga
        fields = ('id', 'titulo', 'descricao', 'salario', 'local', 'quantidade', 'contato', 'tipo_contratacao', 'tecnologias', 'links')
    
    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('vaga-detalhes', kwargs={'id': obj.pk}, request=request),
            'delete': reverse('vaga-detalhes', kwargs={'id': obj.pk}, request=request),
            'put': reverse('vaga-detalhes', kwargs={'id': obj.pk}, request=request),
        }