from rest_framework import serializers
from .models import Item, Category, AddOperation


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


class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOperation
        fields = '__all__'
        read_only_fields = ['result', 'created_at']  # resultado e data de crição são apenas leitura

    def create(self, validated_data):
        # validated_data['result'] = validated_data['valor1'] + validated_data['valor2']
        valor1 = validated_data.get('valor1')
        valor2 = validated_data.get('valor2')
        # Realiza a soma e salva o resultado
        validated_data['result'] = valor1 + valor2
        return super().create(validated_data)
