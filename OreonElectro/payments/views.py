from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from orders.models import Order
from .models import Payment, PaymentStatus
from .serializers import PaymentSerializer


class PaymentView(APIView):
    """
    Create a new payment for an order
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        order_id = data.get('order_id')
        gateway = data.get('gateway')
        amount = data.get('amount')

        order = get_object_or_404(Order, id=order_id, customer=request.user)

        payment_data = {
                'user': request.user.id,
                'order': order.id,
                'gateway': gateway,
                'amount': amount
        }

        serializer = PaymentSerializer(data=payment_data)

        if serializer.is_valid():
            payment = serializer.save()

            # Here will be the logic for processing payments via a gateway
            # For demo we simulate a successful payment
            payment.status = PaymentStatus.COMPLETED
            payment.transaction_id = 'dummy_transaction_id'
            payment.save()

            order.status = 'Completed' # or 'Pending Shipment'
            order.save()

            return Response({'message': 'Payment successful', 'payment_id': payment.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentStatusView(APIView):
    """
    Retrieve the status of a specific payment
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, user=request.user)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserPaymentsView(generics.ListAPIView):
    """
    List all payments made by the authenticated user
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user).order_by('-created_at')
