from rest_framework import viewsets
from .models import ShippingProvider, ShippingOption, ShippingRate
from .serializers import ShippingProviderSerializer, ShippingOptionSerializer, ShippingRateSerializer


class ShippingProviderViewSet(viewsets.ModelViewSet):
    queryset = ShippingProvider.objects.all()
    serializer_class = ShippingProviderSerializer


class ShippingOptionViewSet(viewsets.ModelViewSet):
    queryset = ShippingOption.objects.all()
    serializer_class = ShippingOptionSerializer


class ShippingRateViewSet(viewsets.ModelViewSet):
    queryset = ShippingRate.objects.all()
    serializer_class = ShippingRateSerializer
