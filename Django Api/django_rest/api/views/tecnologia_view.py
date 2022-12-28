from ..pagination import PaginacaoCustomizada
from rest_framework.views import APIView
from ..services import tecnologia_service
from ..serializers import tecnologia_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import tecnologia
from rest_framework.permissions import IsAuthenticated


class TecnologiaList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        #paginacao = PageNumberPagination()
        paginacao = PaginacaoCustomizada()
        tecnologias = tecnologia_service.listar_tecnologias()
        resultado = paginacao.paginate_queryset(tecnologias, request)
        serializer = tecnologia_serializer.TecnologiaSerializer(resultado, context = {'request':request}, many = True)
        return paginacao.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = tecnologia_serializer.TecnologiaSerializer(data = request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome = nome)
            tecnologia_bd = tecnologia_service.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class TecnologiaDetalhes(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        tecnologia_antiga = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia_antiga, data = request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome = nome)
            tecnologia_service.editar_tecnologia(tecnologia_antiga, tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        if tecnologia:
            tecnologia_service.remover_tecnologia(tecnologia)
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)