# reporting/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesReportViewSet, CustomerBehaviorReportViewSet

router = DefaultRouter()
router.register(r'sales', SalesReportViewSet, basename='sales')
router.register(r'customer-behavior', CustomerBehaviorReportViewSet, basename='customer-behavior')

urlpatterns = [
        path('', include(router.urls)),
]
