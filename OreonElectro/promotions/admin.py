from django.contrib import admin
from .models import Discount, Coupon, Promotion


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'active', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active',  'created_at', 'updated_at')
    search_fields = ('code',)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'valid_from', 'valid_to', 'active',  'created_at', 'updated_at')
    search_fields = ('title',)
