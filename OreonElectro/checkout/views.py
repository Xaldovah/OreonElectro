from django.db import transaction
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Checkout
from .serializers import CheckoutSerializer, OrderSerializer, OrderItemSerializer
from cart.models import CartItem
from orders.models import Order, OrderItem


class CheckoutView(APIView):
    """
    checkout method
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CheckoutSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            with transaction.atomic():
                order = serializer.save()
                cart_items = CartItem.objects.filter(cart__user=request.user)
                for cart_item in cart_items:
                    OrderItem.objects.create(
                            order=order,
                            product=cart_item.product,
                            quantity=cart_item.quantity,
                            subtotal=cart_item.subtotal
                    )
                cart_items.delete()
                return Response({'message': 'Order created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class OrderConfirmationView(APIView):
    """
    order confirmation
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            order = Order.objects.filter(customer=request.user).latest('created_at')
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'No recent orders found'}, status=status.HTTP_404_NOT_FOUND)


class OrderDetailView(generics.RetrieveAPIView):
    """
    Retrieve the latest order of the authenticated user
    """
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_object(self):
        return get_object_or_404(Order, customer=self.request.user)


class OrderListView(generics.ListAPIView):
    """
    List all orders of the authenticated user
    """
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')
