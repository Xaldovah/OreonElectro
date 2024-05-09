from rest_framework import serializers
from .models import InventoryItem, StockAlert


class InventoryItemSerializer(serializers.ModelSerializer):
    is_low_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = InventoryItem
        fields = '__all__'


class StockAlertSerializer(serializers.ModelSerializer):
    item = InventoryItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=InventoryItem.objects.all(), write_only=True)

    class Meta:
        model = StockAlert
        fields = ['id', 'item', 'item_id', 'message', 'created_at']
