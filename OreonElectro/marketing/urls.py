# marketing/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailCampaignViewSet, NewsletterSubscriptionViewSet, PromotionalActivityViewSet

router = DefaultRouter()
router.register(r'campaigns', EmailCampaignViewSet, basename='campaign')
router.register(r'subscriptions', NewsletterSubscriptionViewSet, basename='subscription')
router.register(r'promotions', PromotionalActivityViewSet, basename='promotion')

urlpatterns = [
        path('', include(router.urls)),
]
