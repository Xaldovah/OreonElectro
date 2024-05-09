from rest_framework import viewsets
from .models import SalesReport, CustomerBehaviorReport
from .serializers import SalesReportSerializer, CustomerBehaviorReportSerializer


class SalesReportViewSet(viewsets.ModelViewSet):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer


class CustomerBehaviorReportViewSet(viewsets.ModelViewSet):
    queryset = CustomerBehaviorReport.objects.all()
    serializer_class = CustomerBehaviorReportSerializer
