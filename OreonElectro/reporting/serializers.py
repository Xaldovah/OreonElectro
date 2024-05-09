# reporting/serializers.py
from rest_framework import serializers
from .models import SalesReport, CustomerBehaviorReport


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = '__all__'


class CustomerBehaviorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBehaviorReport
        fields = '__all__'
