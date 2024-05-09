from django.contrib import admin
from .models import InventoryItem, StockAlert


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'quantity', 'reorder_level', 'is_low_stock')
    search_fields = ('name', 'sku')
    list_filter = ('quantity', 'reorder_level')
    readonly_fields = ('is_low_stock',)

    def is_low_stock(self, obj):
        return obj.is_low_stock()
    is_low_stock.boolean = True
    is_low_stock.short_description = 'Low Stock'


@admin.register(StockAlert)
class StockAlertAdmin(admin.ModelAdmin):
    list_display = ('item', 'message', 'created_at')
    search_fields = ('item__name', 'message')
    list_filter = ('created_at',)
