from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscountViewSet, CouponViewSet, PromotionViewSet


router = DefaultRouter()
router.register(r'discounts', DiscountViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'promotions', PromotionViewSet)


urlpatterns = [
        path('', include(router.urls)),
]
