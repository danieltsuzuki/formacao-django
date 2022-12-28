from rest_framework import serializers
from ..models import Tecnologia
from rest_framework.reverse import reverse

class TecnologiaSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Tecnologia
        fields = ("id" ,"nome", "links")
    
    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('tecnologia-detalhes', kwargs={'id': obj.pk}, request=request),
            'delete': reverse('tecnologia-detalhes', kwargs={'id': obj.pk}, request=request),
            'put': reverse('tecnologia-detalhes', kwargs={'id': obj.pk}, request=request),
        }