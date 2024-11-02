from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name


class AddOperation(models.Model):
    valor1 = models.DecimalField(max_digits=10, decimal_places=2)
    valor2 = models.DecimalField(max_digits=10, decimal_places=2)
    result = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.valor1} + {self.valor2} = {self.result}'
