from django.contrib import admin
from .models import Item, Category, AddOperation


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(AddOperation)
class AddOperationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'valor1', 'valor2', 'result')
    list_display_links = ('created_at',)
