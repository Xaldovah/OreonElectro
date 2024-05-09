from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import EmailCampaign, NewsletterSubscription, PromotionalActivity


class EmailCampaignTests(APITestCase):
    def setUp(self):
        self.campaign = EmailCampaign.objects.create(
                title='Summer Sale',
                content='Get 50% off on all items this summer!',
                status='draft',
                scheduled_date='2024-06-01T10:00:00Z'
        )
        self.url = reverse('campaign-detail', args=[self.campaign.id])

    def test_get_email_campaign(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Summer Sale')

    def test_create_email_campaign(self):
        data = {
                'title': 'Winter Sale',
                'content': 'Get 30% off on all items this winter!',
                'status': 'draft',
                'scheduled_date': '2024-12-01T10:00:00Z'
        }
        response = self.client.post(reverse('campaign-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Winter Sale')

    def test_update_email_campaign(self):
        data = {
                'title': 'Summer Sale Updated',
                'content': 'Get 60% off on all items this summer!',
                'status': 'scheduled',
                'scheduled_date': '2024-06-01T10:00:00Z'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Summer Sale Updated')

    def test_delete_email_campaign(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(EmailCampaign.objects.filter(id=self.campaign.id).exists())

    def test_send_campaign(self):
        url = reverse('campaign-send-campaign', args=[self.campaign.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'scheduled')


class NewsletterSubscriptionTests(APITestCase):
    def setUp(self):
        self.subscription = NewsletterSubscription.objects.create(
                email='test@example.com',
                is_active=True
        )
        self.url = reverse('subscription-detail', args=[self.subscription.id])

    def test_get_subscription(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_create_subscription(self):
        data = {
                'email': 'new@example.com',
                'is_active': True
        }
        response = self.client.post(reverse('subscription-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], 'new@example.com')

    def test_update_subscription(self):
        data = {
                'email': 'test@example.com',
                'is_active': False
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_active'], False)

    def test_delete_subscription(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(NewsletterSubscription.objects.filter(id=self.subscription.id).exists())

    def test_unsubscribe(self):
        url = reverse('subscription-unsubscribe', args=[self.subscription.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'unsubscribed')


class PromotionalActivityTests(APITestCase):
    def setUp(self):
        self.activity = PromotionalActivity.objects.create(
                name='Black Friday Sale',
                description='Get up to 80% off on all items during the Black Friday Sale!',
                start_date='2024-11-22',
                end_date='2024-11-28'
        )
        self.url = reverse('promotion-detail', args=[self.activity.id])

    def test_get_promotional_activity(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Black Friday Sale')

    def test_create_promotional_activity(self):
        data = {
                'name': 'Christmas Sale',
                'description': 'Get up to 70% off on all items during the Christmas Sale!',
                'start_date': '2024-12-20',
                'end_date': '2024-12-25'
        }
        response = self.client.post(reverse('promotion-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Christmas Sale')

    def test_update_promotional_activity(self):
        data = {
                'name': 'Black Friday Sale Updated',
                'description': 'Get up to 90% off on all items during the Black Friday Sale!',
                'start_date': '2024-11-22',
                'end_date': '2024-11-29'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Black Friday Sale Updated')

    def test_delete_promotional_activity(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(PromotionalActivity.objects.filter(id=self.activity.id).exists())
