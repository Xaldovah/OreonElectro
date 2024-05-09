from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SEOViewSet


router = DefaultRouter()
router.register(r'seo', SEOViewSet, basename='seo')


urlpatterns = [
        path('', include(router.urls)),
]
