from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from .models import Item, Category, AddOperation
from .serializers import ItemSerializer, CategorySerializer, AddSerializer
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
    search_fields = ['name', 'category__name']  # Campos que podem ser buscados


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AddView(viewsets.ModelViewSet):
    queryset = AddOperation.objects.all().order_by('-created_at')
    serializer_class = AddSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit', None)
        queryset = self.get_queryset()

        if limit is not None:
            queryset = queryset[:int(limit)]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
