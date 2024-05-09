# seo/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SEO


class SEOTests(APITestCase):
    def setUp(self):
        self.seo = SEO.objects.create(
                page='home',
                meta_title='Home Page',
                meta_description='This is the homepage.',
                meta_keywords='home,homepage',
                meta_robots='index,follow'
        )
        self.url = reverse('seo-detail', args=[self.seo.page])

    def test_get_seo(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['page'], 'home')

    def test_create_seo(self):
        data = {
                'page': 'about',
                'meta_title': 'About Us',
                'meta_description': 'This is the about page.',
                'meta_keywords': 'about,company,info',
                'meta_robots': 'index,follow'
        }
        response = self.client.post(reverse('seo-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['page'], 'about')

    def test_update_seo(self):
        data = {
                'page': 'home',
                'meta_title': 'Updated Home Page',
                'meta_description': 'This is the updated homepage.',
                'meta_keywords': 'home,homepage,updated',
                'meta_robots': 'index,follow'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['meta_title'], 'Updated Home Page')

    def test_delete_seo(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SEO.objects.filter(page='home').exists())
