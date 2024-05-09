from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost, FAQ, StaticPage


class BlogPostTests(APITestCase):
    def setUp(self):
        self.blog_post = BlogPost.objects.create(
                title='First Blog',
                slug='first-blog',
                content='Content of the first blog.',
                author='Admin'
        )
        self.url = reverse('blog-detail', args=[self.blog_post.slug])

    def test_get_blog_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'First Blog')

    def test_create_blog_post(self):
        data = {
                'title': 'Second Blog',
                'slug': 'second-blog',
                'content': 'Content of the second blog.',
                'author': 'Admin'
        }
        response = self.client.post(reverse('blog-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Second Blog')

    def test_update_blog_post(self):
        data = {
                'title': 'Updated First Blog',
                'slug': 'first-blog',
                'content': 'Updated content of the first blog.',
                'author': 'Admin'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated First Blog')

    def test_delete_blog_post(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(BlogPost.objects.filter(slug='first-blog').exists())


class FAQTests(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
                question='What is this?',
                answer='This is a FAQ.'
        )
        self.url = reverse('faq-detail', args=[self.faq.id])

    def test_get_faq(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], 'What is this?')

    def test_create_faq(self):
        data = {
                'question': 'How does this work?',
                'answer': 'It works like this.'
        }
        response = self.client.post(reverse('faq-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['question'], 'How does this work?')

    def test_update_faq(self):
        data = {
                'question': 'Updated Question',
                'answer': 'Updated Answer'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], 'Updated Question')

    def test_delete_faq(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FAQ.objects.filter(id=self.faq.id).exists())


class StaticPageTests(APITestCase):
    def setUp(self):
        self.static_page = StaticPage.objects.create(
                title='About Us',
                slug='about-us',
                content='Content about us.'
        )
        self.url = reverse('static-detail', args=[self.static_page.slug])

    def test_get_static_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'About Us')

    def test_create_static_page(self):
        data = {
                'title': 'Contact Us',
                'slug': 'contact-us',
                'content': 'Content for contact us page.'
        }
        response = self.client.post(reverse('static-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Contact Us')

    def test_update_static_page(self):
        data = {
                'title': 'Updated About Us',
                'slug': 'about-us',
                'content': 'Updated content about us.'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated About Us')

    def test_delete_static_page(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(StaticPage.objects.filter(slug='about-us
