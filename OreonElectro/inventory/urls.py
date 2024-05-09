# inventory/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, StockAlertViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet, basename='item')
router.register(r'alerts', StockAlertViewSet, basename='alert')

urlpatterns = [
        path('', include(router.urls)),
]
