from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShippingProviderViewSet, ShippingOptionViewSet, ShippingRateViewSet


router = DefaultRouter()
router.register(r'providers', ShippingProviderViewSet, basename='provider')
router.register(r'options', ShippingOptionViewSet, basename='option')
router.register(r'rates', ShippingRateViewSet, basename='rate')

urlpatterns = [
        path('', include(router.urls)),
]
