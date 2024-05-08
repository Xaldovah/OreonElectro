from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as django_filters
from .models import Discount, Coupon, Promotion
from .serializers import DiscountSerializer, CouponSerializer, PromotionSerializer


class DiscountFilter(django_filters.FilterSet):
    class Meta:
        model = Discount
        fields = {
                'name': ['icontains'],
                'percentage': ['exact', 'gte', 'lte'],
                'active': ['exact'],
        }


class CouponFilter(django_filters.FilterSet):
    class Meta:
        model = Coupon
        fields = {
                'code': ['icontains'],
                'discount__name': ['icontains'],
                'active': ['exact'],
                'valid_from': ['gte', 'lte'],
                'valid_to': ['gte', 'lte'],
        }


class PromotionFilter(django_filters.FilterSet):
    class Meta:
        model = Promotion
        fields = {
                'title': ['icontains'],
                'discount__name': ['icontains'],
                'active': ['exact'],
                'valid_from': ['gte', 'lte'],
                'valid_to': ['gte', 'lte'],
        }


class DiscountViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = DiscountFilter
    search_fields = ['name']
    ordering_fields = ['name', 'percentage', 'created_at', 'updated_at']


class CouponViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CouponFilter
    search_fields = ['code', 'discount__name']
    ordering_fields = ['code', 'valid_from', 'valid_to', 'created_at', 'updated_at']


class PromotionViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PromotionFilter
    search_fields = ['title', 'discount__name']
    ordering_fields = ['title', 'valid_from', 'valid_to', 'created_at', 'updated_at']
