# shipping/admin.py
from django.contrib import admin
from .models import ShippingProvider, ShippingOption, ShippingRate


@admin.register(ShippingProvider)
class ShippingProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)


@admin.register(ShippingOption)
class ShippingOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'is_active')
    list_filter = ('provider', 'is_active')
    search_fields = ('name',)


@admin.register(ShippingRate)
class ShippingRateAdmin(admin.ModelAdmin):
    list_display = ('option', 'weight_min', 'weight_max', 'rate')
    list_filter = ('option',)
    search_fields = ('option__name',)
