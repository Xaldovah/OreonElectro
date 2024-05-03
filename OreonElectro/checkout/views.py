from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CheckoutSerializer, OrderSerializer
from cart.models import CartItem
from orders.models import Order, OrderItem


class CheckoutView(APIView):
    """
    checkout method
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping_address = form.cleaned_data['shipping_address']
            billing_address = form.cleaned_data['billing_address']
            payment_method = form.cleaned_data['payment_method']

            order_data = {
                    'customer': request.user,
                    'shipping_address': shipping_address,
                    'billing_address': billing_address,
                    'payment_method': payment_method,
                    'status': 'Pending'
            }
            
            serializer = CheckoutSerializer(data=order_data)
            if serializer.is_valid():
                order = serializer.save()

                for cart_item in request.user.cart.items.all():
                    OrderItem.objects.create(
                            order=order,
                            product=cart_item.product,
                            quantity=cart_item.quantity,
                            subtotal=cart_item.subtotal
                    )

                request.user.cart.clear()

                return Response({'message': 'Order created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)


class OrderConfirmationView(APIView):
    """
    order confirmation
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(customer=request.user).latest('created_at')
        serializer = OrderSerializer(order)
        return Response(serializer.data)
