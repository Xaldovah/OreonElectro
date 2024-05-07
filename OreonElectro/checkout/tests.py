from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Checkout
from orders.models import Order, OrderItem
from products.Product import Product
from cart.models import Cart, CartItem

User = get_user_model()


class CheckoutTests(APITestCase):

    def setup(self):
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.cart = Cart.objects.create(self=self.user)
        self.product = Product.objects.create(name='Test Product', price=100)
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=2, subtotal=200)

    def test_create_order(self):
        url = reverse('checkout')
        data = {
                'shipping_address': '123 Test St.',
                'billing_address': '123 Test St.',
                'payment_method': 'M-Pesa'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)


    def test_latest_order(self):
        order = Order.objects.create(customer=self.user, shipping_address='123 Test St.', billing_address='123 Test St.', payment_method='M-Pesa')
        OrderItem.objects.create(order=order, product=self.product, quantity=2, subtotal=200)

        url = reverse('latest-order')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['shipping_address'], '123 Test St.')
