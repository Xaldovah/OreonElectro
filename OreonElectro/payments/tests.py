from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from orders.models import Order
from .models import Payment, PaymentGateway, PaymentStatus

User = get_user_model()

class PaymentTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.order = Order.objects.create(
                customer=self.user,
                shipping_address='123 Test St.',
                billing_address='123 Test Ave.',
                payment_method='Credit Card',
                status='Pending'
        )

    def test_create_payment(self):
        url = reverse('payment')
        data = {
                'order_id': self.order.id,
                'gateway': PaymentGateway.PAYPAL,
                'amount': 100
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)
        payment = Payment.objects.first()
        self.assertEqual(payment.status, PaymentStatus.COMPLETED)

    def test_payment_status(self):
        payment = Payment.objects.create(
                user=self.user,
                order=self.order,
                gateway=PaymentGateway.STRIPE,
                amount=100,
                status=PaymentStatus.COMPLETED,
                transaction_id='dummy_txn_id'
        )
        url = reverse('payment-status', args=[payment.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], PaymentStatus.COMPLETED)
                                                                          
    def test_user_payments(self):
        Payment.objects.create(
                user=self.user,
                order=self.order,
                gateway=PaymentGateway.STRIPE,
                amount=100,
                status=PaymentStatus.COMPLETED,
                transaction_id='dummy_txn_id'
        )

        url = reverse('user-payments')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
