from rest_framework import serializers
from .models import Item, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        item = Item.objects.create(category=category, **validated_data)
        return item

    def update(self, instance, validated_data):
        # Extrai e remove os dados da categoria do validated_data
        category_data = validated_data.pop('category', None)

        # Atualiza os campos do item
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        # Lida com a categoria aninhada
        if category_data:
            category_name = category_data.get('name')
            # Busca a categoria ou cria uma nova com o nome fornecido
            category, created = Category.objects.get_or_create(name=category_name)
            instance.category = category
        instance.save()
        return instance
