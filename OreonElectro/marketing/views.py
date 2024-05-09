from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import EmailCampaign, NewsletterSubscription, PromotionalActivity
from .serializers import EmailCampaignSerializer, NewsletterSubscriptionSerializer, PromotionalActivitySerializer


class EmailCampaignViewSet(viewsets.ModelViewSet):
    queryset = EmailCampaign.objects.all()
    serializer_class = EmailCampaignSerializer

    @action(detail=True, methods=['post'], url_path='send')
    def send_campaign(self, request, pk=None):
        campaign = self.get_object()
        if campaign.status == 'draft':
            campaign.status = 'scheduled'
            campaign.save()
            return Response({'status': 'scheduled'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Campaign already sent or scheduled'}, status=status.HTTP_400_BAD_REQUEST)


class NewsletterSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer

    @action(detail=True, methods=['post'], url_path='unsubscribe')
    def unsubscribe(self, request, pk=None):
        subscription = self.get_object()
        subscription.is_active = False
        subscription.save()
        return Response({'status': 'unsubscribed'}, status=status.HTTP_200_OK)


class PromotionalActivityViewSet(viewsets.ModelViewSet):
    queryset = PromotionalActivity.objects.all()
    serializer_class = PromotionalActivitySerializer
