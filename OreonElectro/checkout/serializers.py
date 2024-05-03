from rest_framework import serializers
from orders.models import Order


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'shipping_address', 'billing_address', 'payment_method', 'status']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'shipping_address', 'billing_address', 'payment_method', 'status', 'created_at', 'updated_at']
