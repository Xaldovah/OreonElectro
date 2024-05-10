import unittest
from django.test import Client, RequestFactory
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Customer
from .views import RegisterView, LoginView, LogoutView, PasswordResetView, CustomerDetailView


class TestUserModels(unittest.TestCase):
    def test_customer_model(self):
        # Test creating a customer
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        customer = Customer.objects.create(
                user=user,
                shipping_address='123 Main St',
                billing_address='456 Oak Rd',
                email='testuser@example.com',
                phone_number='+1234567890',
                payment_method='mpesa'
        )
        self.assertEqual(customer.user, user)
        self.assertEqual(customer.shipping_address, '123 Main St')
        self.assertEqual(customer.billing_address, '456 Oak Rd')
        self.assertEqual(customer.email, 'testuser@example.com')
        self.assertEqual(customer.phone_number, '+1234567890')
        self.assertEqual(customer.payment_method, 'mpesa')

        # Test edge case: creating a customer with an invalid phone number
        with self.assertRaises(ValueError):
            Customer.objects.create(
                    user=user,
                    shipping_address='123 Main St',
                    billing_address='456 Oak Rd',
                    email='testuser@example.com',
                    phone_number='1234',
                    payment_method='mpesa'
            )


class TestUserViews(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_register_view(self):
        # Test the POST method
        data = {
                'username': 'testuser',
                'email': 'testuser@example.com',
                'password': 'testpassword',
                'shipping_address': '123 Main St',
                'billing_address': '456 Oak Rd',
                'phone_number': '+1234567890',
                'payment_method': 'mpesa'
        }
        request = self.factory.post(reverse('register'), data=data, content_type='application/json')
        response = RegisterView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User created successfully!')

        # Test edge case: registering a user with invalid data
        data = {
                'username': '',
                'email': 'testuser@example.com',
                'password': 'testpassword',
                'shipping_address': '123 Main St',
                'billing_address': '456 Oak Rd',
                'phone_number': '1234',
                'payment_method': 'mpesa'
        }
        request = self.factory.post(reverse('register'), data=data, content_type='application/json')
        response = RegisterView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_view(self):
        # Test the POST method
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        data = {
                'username': 'testuser',
                'password': 'testpassword'
        }
        request = self.factory.post(reverse('login'), data=data, content_type='application/json')
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        # Test edge case: logging in with invalid credentials
        data = {
                'username': 'invaliduser',
                'password': 'invalidpassword'
        }
        request = self.factory.post(reverse('login'), data=data, content_type='application/json')
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'error': 'Invalid credentials'})

    def test_logout_view(self):
        # Test the POST method
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = self.factory.post(reverse('logout'))
        response = LogoutView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Logout successful!'})

        # Test edge case: logging out an unauthenticated user
        self.client.logout()
        request = self.factory.post(reverse('logout'))
        response = LogoutView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_password_reset_view(self):
        # Test the POST method
        data = {
                'email': 'testuser@example.com'
        }
        request = self.factory.post(reverse('password-reset'), data=data, content_type='application/json')
        response = PasswordResetView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Password reset email sent'})

        # Test edge case: password reset with an invalid email
        data = {
                'email': 'invaliduser@example.com'
        }
        request = self.factory.post(reverse('password-reset'), data=data, content_type='application/json')
        response = PasswordResetView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_detail_view(self):
        # Test the GET method
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        customer = Customer.objects.create(
                user=user,
                shipping_address='123 Main St',
                billing_address='456 Oak Rd',
                email='testuser@example.com',
                phone_number='+1234567890',
                payment_method='mpesa'
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = self.factory.get(reverse('customer-detail'))
        response = CustomerDetailView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['shipping_address'], '123 Main St')

        # Test the PUT method
        data = {
                'shipping_address': '789 Elm St',
                'billing_address': '321 Oak Rd',
                'phone_number': '+0987654321'
        }
        request = self.factory.put(reverse('customer-detail'), data=data, content_type='application/json')
        response = CustomerDetailView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['shipping_address'], '789 Elm St')
        self.assertEqual(response.data['billing_address'], '321 Oak Rd')
        self.assertEqual(response.data['phone_number'], '+0987654321')

        # Test edge case: updating customer details with invalid data
        data = {
                'shipping_address': '789 Elm St',
                'billing_address': '321 Oak Rd',
                'phone_number': '1234'
        }
        request = self.factory.put(reverse('customer-detail'), data=data, content_type='application/json')
        response = CustomerDetailView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test edge case: accessing customer detail view without authentication
        self.client.logout()
        request = self.factory.get(reverse('customer-detail'))
        response = CustomerDetailView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

if __name__ == '__main__':
    unittest.main()
