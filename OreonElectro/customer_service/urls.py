# customer_service/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupportTicketViewSet, ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'tickets', SupportTicketViewSet, basename='ticket')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
        path('', include(router.urls)),
]
