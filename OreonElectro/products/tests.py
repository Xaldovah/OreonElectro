import unittest
from django.test import Client, RequestFactory
from django.urls import reverse
from rest_framework import status
from .models import Category, Product
from .views import ProductListView, ProductDetailView, ProductPricingView, ProductInventoryView, SearchView


class TestProductModels(unittest.TestCase):
    def test_category_model(self):
        category = Category.objects.create(name="Electronics", description="Electronic products")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic products")

        with self.assertRaises(ValueError):
            Category.objects.create(name="", description="Empty name")

    def test_product_model(self):
        category = Category.objects.create(name="Electronics", description="Electronic products")
        product = Product.objects.create(
                name="Laptop", description="A powerful laptop", price=50000, stock_quantity=10, category=category
        )
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "A powerful laptop")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.stock_quantity, 10)
        self.assertEqual(product.category, category)

        with self.assertRaises(ValueError):
            Product.objects.create(
                    name="Laptop", description="A powerful laptop", price=50000, stock_quantity=-5, category=category
            )


class TestProductViews(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        self.category = Category.objects.create(name="Electronics", description="Electronic products")
        self.product1 = Product.objects.create(
                name="Laptop", description="A powerful laptop", price=50000, stock_quantity=10, category=self.category
        )
        self.product2 = Product.objects.create(
                name="Smartphone", description="A high-end smartphone", price=30000, stock_quantity=20, category=self.category
        )

    def test_product_list_view(self):
        request = self.factory.get(reverse('product-list'))
        response = ProductListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        data = {
                "name": "Tablet",
                "description": "A tablet device",
                "price": 20000,
                "stock_quantity": 15,
                "category": self.category.id
        }
        request = self.factory.post(reverse('product-list'), data=data, content_type='application/json')
        response = ProductListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Tablet')

        data = {
                "name": "",
                "description": "A tablet device",
                "price": 20000,
                "stock_quantity": 15,
                "category": self.category.id
        }
        request = self.factory.post(reverse('product-list'), data=data, content_type='application/json')
        response = ProductListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_product_detail_view(self):
        request = self.factory.get(reverse('product-detail', args=[self.product1.id]))
        response = ProductDetailView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product1.name)

        data = {
                "name": "Updated Laptop",
                "description": "An updated powerful laptop",
                "price": 55000,
                "stock_quantity": 15,
                "category": self.category.id
        }
        request = self.factory.put(reverse('product-detail', args=[self.product1.id]), data=data, content_type='application/json')
        response = ProductDetailView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Laptop')

        request = self.factory.delete(reverse('product-detail', args=[self.product1.id]))
        response = ProductDetailView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        request = self.factory.get(reverse('product-detail', args=[100]))
        response = ProductDetailView.as_view()(request, pk=100)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_product_pricing_view(self):
        data = {
                "price": 60000
        }
        request = self.factory.put(reverse('product-pricing', args=[self.product1.id]), data=data, content_type='application/json')
        response = ProductPricingView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=self.product1.id).price, 60000)

        data = {
                "price": -10000
        }
        request = self.factory.put(reverse('product-pricing', args=[self.product1.id]), data=data, content_type='application/json')
        response = ProductPricingView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_product_inventory_view(self):
        data = {
                "stock_quantity": 25
        }
        request = self.factory.put(reverse('product-inventory', args=[self.product1.id]), data=data, content_type='application/json')
        response = ProductInventoryView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=self.product1.id).stock_quantity, 25)

        data = {
                "stock_quantity": -10
        }
        request = self.factory.put(reverse('product-inventory', args=[self.product1.id]), data=data, content_type='application/json')
        response = ProductInventoryView.as_view()(request, pk=self.product1.id)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_view(self):
        request = self.factory.get(reverse('search') + '?query=Laptop')
        response = SearchView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Laptop')

        data = {
                "query": "Smartphone"
        }
        request = self.factory.post(reverse('search'), data=data, content_type='application/json')
        response = SearchView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Smartphone')

        data = {
                "query": ""
        }
        request = self.factory.post(reverse('search'), data=data, content_type='application/json')
        response = SearchView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Invalid form data'})

        self.client.logout()
        request = self.factory.get(reverse('search') + '?query=Laptop')
        response = SearchView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

if __name__ == '__main__':
    unittest.main()
