from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from products.models import Product


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
        orders = Order.objects.filter(customer=user)
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
            order_items_data = serializer.validated_data.pop('order_items')
            order = serializer.save(customer=request.user)

            for order_item_data in order_items_data:
                product = Product.objects.get(pk=order_item_data['product'])
                order_item = OrderItem(order=order, product=product, quantity=order_item_data['quantity'])
                order_item.save()

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


class FulfillOrderView(APIView):
    """
    API endpoint to fulfill an order.

    Args:
        APIView: HTTP request object.

    Return:
        Response: JSON response containing fulfilled order.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.customer != request.user:
            return Response({'error': 'You are not authorized to fulfill this order'}, status=status.HTTP_403_FORBIDDEN)

        if order.fulfillment_status != Order.PROCESSING:
            return Response({'error': 'Order is not in processsing state'}, status=status.HTTP_400_BAD_REQUEST)

        order.fulfillment_status = Order.SHIPPED
        order.tracking_number = request.data.get('tracking_number')
        order.save()
        # will implement email notification and email sending here
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class UpdateOrderStatusView(APIView):
    """
    API endpoint to update the status of an order.

    Args:
        APIView: HTTP request object.
        pk: Primary key of the order to update.

    Returns:
        Response: JSON response containing updated order status.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.customer != request.user:
            return Response({'error': 'You are not authorized to update this order'}, status=status.HTTP_403_FORBIDDEN)
        new_status = request.data.get('status')
        if new_status in Order.ORDER_STATUS_CHOICES:
            order.status = new_status
            order.save()
            return Response({'status': order.status}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)


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
