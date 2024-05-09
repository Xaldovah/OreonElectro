from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ShippingProvider, ShippingOption, ShippingRate


class ShippingProviderTests(APITestCase):
    def setUp(self):
        self.provider = ShippingProvider.objects.create(name='DHL', website='https://dhl.com')
        self.url = reverse('provider-detail', args=[self.provider.id])

    def test_get_provider(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'DHL')

    def test_create_provider(self):
        data = {
                'name': 'FedEx',
                'website': 'https://fedex.com'
        }
        response = self.client.post(reverse('provider-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'FedEx')

    def test_update_provider(self):
        data = {
                'name': 'Updated DHL',
                'website': 'https://dhl.com'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated DHL')

    def test_delete_provider(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ShippingProvider.objects.filter(id=self.provider.id).exists())


class ShippingOptionTests(APITestCase):
    def setUp(self):
        self.provider = ShippingProvider.objects.create(name='DHL', website='https://dhl.com')
        self.option = ShippingOption.objects.create(name='Express', provider=self.provider, description='Fast shipping')
        self.url = reverse('option-detail', args=[self.option.id])

    def test_get_option(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Express')

    def test_create_option(self):
        data = {
                'name': 'Standard',
                'provider_id': self.provider.id,
                'description': 'Affordable shipping',
                'is_active': True
        }
        response = self.client.post(reverse('option-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Standard')

    def test_update_option(self):
        data = {
                'name': 'Updated Express',
                'provider_id': self.provider.id,
                'description': 'Updated fast shipping',
                'is_active': True
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Express')

    def test_delete_option(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ShippingOption.objects.filter(id=self.option.id).exists())


class ShippingRateTests(APITestCase):
    def setUp(self):
        self.provider = ShippingProvider.objects.create(name='DHL', website='https://dhl.com')
        self.option = ShippingOption.objects.create(name='Express', provider=self.provider, description='Fast shipping')
        self.rate = ShippingRate.objects.create(option=self.option, weight_min=0.0, weight_max=5.0, rate=20.0)
        self.url = reverse('rate-detail', args=[self.rate.id])

    def test_get_rate(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rate'], '20.00')

    def test_create_rate(self):
        data = {
                'option_id': self.option.id,
                'weight_min': 5.0,
                'weight_max': 10.0,
                'rate': 35.0
        }
        response = self.client.post(reverse('rate-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['rate'], '35.00')

    def test_update_rate(self):
        data = {
                'option_id': self.option.id,
                'weight_min': 0.0,
                'weight_max': 5.0,
                'rate': 25.0
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rate'], '25.00')

    def test_delete_rate(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ShippingRate.objects.filter(id=self.rate.id).exists())
