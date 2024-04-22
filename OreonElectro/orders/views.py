from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def order_history(request):
    """
    API endpoint to retrieve order history for the authenticated user.

    Args:
        request: HTTP request object.

    Returns:
        Response: JSON response containing order history.
    """
    user = request.user
    orders = Order.objects.filter(customer__user=user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
