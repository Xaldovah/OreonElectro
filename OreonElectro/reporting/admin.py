from django.contrib import admin
from .models import SalesReport, CustomerBehaviorReport


@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_sales', 'total_revenue', 'created_at')
    search_fields = ('date', 'total_sales', 'total_revenue')
    list_filter = ('date',)


@admin.register(CustomerBehaviorReport)
class CustomerBehaviorReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'new_customers', 'returning_customers', 'total_orders', 'total_revenue', 'created_at')
    search_fields = ('date', 'new_customers', 'returning_customers', 'total_orders', 'total_revenue')
    list_filter = ('date',)
