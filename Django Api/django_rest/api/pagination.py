from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginacaoCustomizada(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'tamanho_pagina'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'Links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
        'results': data
        })