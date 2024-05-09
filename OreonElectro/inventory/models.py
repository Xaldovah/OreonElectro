from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f'{self.name} (SKU: {self.sku})'


    def is_low_stock(self):
        return self.quantity <= self.reorder_level


class StockAlert(models.Model):
    item = models.OneToOneField(InventoryItem, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Alert for {self.item.name}'
