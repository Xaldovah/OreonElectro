from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderHistoryView(APIView):
    """
    API endpoint to retrieve order history for the authenticated user.

    Args:
        APIView: HTTP request object.

    Returns:
        Response: JSON response containing order history.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(customer__user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class CreateOrderView(APIView):
    """
    API endpoint to create order for the authenticated user.

    Args:
        APIView: HTTP request object.

    Returns:
        Response: JSON response containing order history.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrderView(APIView):
    """
    API endpoint to update order for the authenticated user.

    Args:
        APIView: HTTP request object.

    Returns:
        Response: JSON response containing order history.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.customer != request.user:
            return Response({'error': 'You are not authorized to update this order'}, status=status.HTTP_403_FORBIDDEN)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteOrderView(APIView):
    """
    API endpoint to delete order for the authenticated user.

    Args:
        APIView: HTTP request object.

    Returns:
        Response: JSON response containing order history.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.customer != request.user:
            return Response({'error': 'You are not authorized to delete this order'}, status=status.HTTP_403_FORBIDDEN)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
