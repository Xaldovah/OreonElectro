from django.db import models


class SalesReport(models.Model):
    date = models.DateField(unique=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sales Report - {self.date}'


class CustomerBehaviorReport(models.Model):
    date = models.DateField(unique=True)
    new_customers = models.PositiveIntegerField()
    returning_customers = models.PositiveIntegerField()
    total_orders = models.PositiveIntegerField()
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer Behavior Report - {self.date}'
