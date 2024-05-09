from rest_framework import serializers
from .models import SEO


class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = '__all__'
