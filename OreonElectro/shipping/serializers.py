from rest_framework import serializers
from .models import ShippingProvider, ShippingOption, ShippingRate


class ShippingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingProvider
        fields = '__all__'


class ShippingOptionSerializer(serializers.ModelSerializer):
    provider = ShippingProviderSerializer(read_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(queryset=ShippingProvider.objects.all(), write_only=True)

    class Meta:
        model = ShippingOption
        fields = ['id', 'name', 'provider', 'provider_id', 'description', 'is_active']


class ShippingRateSerializer(serializers.ModelSerializer):
    option = ShippingOptionSerializer(read_only=True)
    option_id = serializers.PrimaryKeyRelatedField(queryset=ShippingOption.objects.all(), write_only=True)

    class Meta:
        model = ShippingRate
        fields = ['id', 'option', 'option_id', 'weight_min', 'weight_max', 'rate']
