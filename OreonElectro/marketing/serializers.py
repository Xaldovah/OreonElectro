from rest_framework import serializers
from .models import EmailCampaign, NewsletterSubscription, PromotionalActivity


class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCampaign
        fields = '__all__'


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = '__all__'


class PromotionalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionalActivity
        fields = '__all__'
