from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class HelloDRFView(APIView):
    def get(self, request):
        return Response({"message": "Hello DRF!"})

# Sem serializer
# class ItemListView(APIView):
#     def get(self, request):
#         items = [
#             {'id': 1, 'name': 'Item 1', 'description': 'Descrição do Item 1'},
#             {'id': 2, 'name': 'Item 2', 'description': 'Descrição do Item 2'},
#             {'id': 3, 'name': 'Item 3', 'description': 'Descrição do Item 3'},
#         ]
#         return Response(items)

# Com serializer e APIView
# class ItemListView(APIView):
#     def get(self, request):
#         items = Item.objects.all()  # Recupera todos os itens do banco de dados
#         serializer = ItemSerializer(items, many=True)  # Serializa a lista de itens
#         return Response(serializer.data)  # Retorna os dados serializados


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Adiciona os backends de filtro
    filterset_fields = ['name', 'category']  # Campos que podem ser filtrados
    search_fields = ['name', 'description']  # Campos que podem ser buscados


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
