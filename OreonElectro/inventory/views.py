from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import InventoryItem, StockAlert
from .serializers import InventoryItemSerializer, StockAlertSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    @action(detail=True, methods=['post'], url_path='update-stock')
    def update_stock(self, request, pk=None):
        try:
            item = self.get_object()
            quantity = int(request.data.get('quantity', 0))
            if quantity < 0:
                return Response({'detail': 'Quantity must be non-negative.'}, status=status.HTTP_400_BAD_REQUEST)

            item.quantity = quantity
            item.save()

            if item.is_low_stock() and not StockAlert.objects.filter(item=item).exists():
                StockAlert.objects.create(item=item, message=f'{item.name} is low in stock with only {item.quantity} units left.')

            serializer = self.get_serializer(item)
            return Response(serializer.data)
        except (KeyError, ValueError):
            return Response({'detail': 'Invalid quantity provided.'}, status=status.HTTP_400_BAD_REQUEST)


class StockAlertViewSet(viewsets.ModelViewSet):
    queryset = StockAlert.objects.all()
    serializer_class = StockAlertSerializer
