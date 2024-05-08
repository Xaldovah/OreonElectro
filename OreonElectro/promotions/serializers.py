from rest_framework import serializers
from django.utils import timezone
from .models import Discount, Coupon, Promotion


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

    def validate_percentage(self, value):
        if value <= 0 or value > 100:
            raise serializers.ValidationError("Percentage must be between 0 and 100.")
        return value


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

    def validate_code(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Coupon code must be alphanumeric.")
        return value

    def validate(self, data):
        if data['valid_from'] >= data['valid_to']:
            raise serializers.ValidationError("`valid_from` date must be earlier than `valid_to  date.")
        return data


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

    def validate(self, data):
        if data['valid_from'] >= data['valid_to']:
            raise serializers.ValidationError("`valid_from` date must be earlier than `valid_to  date.")
        return data
