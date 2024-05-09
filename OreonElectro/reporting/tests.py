from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SalesReport, CustomerBehaviorReport


class SalesReportTests(APITestCase):
    def setUp(self):
        self.report = SalesReport.objects.create(
                date='2024-05-01',
                total_sales=100,
                total_revenue=5000.00
        )
        self.url = reverse('sales-detail', args=[self.report.id])

    def test_get_sales_report(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_sales'], '100')

    def test_create_sales_report(self):
        data = {
                'date': '2024-05-02',
                'total_sales': 150,
                'total_revenue': 7500.00
        }
        response = self.client.post(reverse('sales-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['total_sales'], '150')

    def test_update_sales_report(self):
        data = {
                'date': '2024-05-01',
                'total_sales': 200,
                'total_revenue': 10000.00
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_sales'], '200')

    def test_delete_sales_report(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SalesReport.objects.filter(id=self.report.id).exists())


class CustomerBehaviorReportTests(APITestCase):
    def setUp(self):
        self.report = CustomerBehaviorReport.objects.create(
                date='2024-05-01',
                new_customers=20,
                returning_customers=30,
                total_orders=50,
                total_revenue=2500.00
        )
        self.url = reverse('customer-behavior-detail', args=[self.report.id])

    def test_get_customer_behavior_report(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['new_customers'], 20)

    def test_create_customer_behavior_report(self):
        data = {
                'date': '2024-05-02',
                'new_customers': 25,
                'returning_customers': 35,
                'total_orders': 60,
                'total_revenue': 3000.00
        }
        response = self.client.post(reverse('customer-behavior-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['new_customers'], 25)

    def test_update_customer_behavior_report(self):
        data = {
                'date': '2024-05-01',
                'new_customers': 30,
                'returning_customers': 40,
                'total_orders': 70,
                'total_revenue': 3500.00
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['new_customers'], 30)

    def test_delete_customer_behavior_report(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CustomerBehaviorReport.objects.filter(id=self.report.id).exists())
