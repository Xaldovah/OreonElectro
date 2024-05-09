from rest_framework import viewsets
from .models import SEO
from .serializers import SEOSerializer


class SEOViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    lookup_field = 'page'
