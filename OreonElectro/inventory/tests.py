from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import InventoryItem, StockAlert


class InventoryItemTests(APITestCase):
    def setUp(self):
        self.item = InventoryItem.objects.create(
                name='Test Product',
                sku='TP001',
                description='A test product',
                quantity=50,
                reorder_level=10
        )
        self.url = reverse('item-detail', args=[self.item.id])

    def test_get_item(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')

    def test_create_item(self):
        data = {
                'name': 'New Product',
                'sku': 'NP001',
                'description': 'A new product',
                'quantity': 20,
                'reorder_level': 5
        }
        response = self.client.post(reverse('item-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Product')

    def test_update_item(self):
        data = {
                'name': 'Updated Product',
                'sku': 'TP001',
                'description': 'An updated product',
                'quantity': 30,
                'reorder_level': 15
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Product')

    def test_delete_item(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(InventoryItem.objects.filter(id=self.item.id).exists())

    def test_update_stock(self):
        url = reverse('item-update-stock', args=[self.item.id])
        data = {'quantity': 8}  # Below reorder level
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 8)
        self.assertTrue(StockAlert.objects.filter(item=self.item).exists())


class StockAlertTests(APITestCase):
    def setUp(self):
        self.item = InventoryItem.objects.create(
                name='Test Product',
                sku='TP001',
                description='A test product',
                quantity=8,
                reorder_level=10
        )
        self.alert = StockAlert.objects.create(
                item=self.item,
                message='Test Product is low in stock with only 8 units left.'
        )
        self.url = reverse('alert-detail', args=[self.alert.id])

    def test_get_alert(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Test Product is low in stock with only 8 units left.')

    def test_create_alert(self):
        data = {
                'item_id': self.item.id,
                'message': 'Test Product is running out quickly!'
        }
        response = self.client.post(reverse('alert-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Test Product is running out quickly!')

    def test_update_alert(self):
        data = {
                'item_id': self.item.id,
                'message': 'Test Product is extremely low in stock!'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Test Product is extremely low in stock!')

    def test_delete_alert(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(StockAlert.objects.filter(id=self.alert.id).exists())
