from django.test import TestCase, Client
from django.urls import reverse
from core.models import Category, Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="pants", slug="pants")
        self.product = Product.objects.create(category=self.category, id=10, name='testshirt', slug='testshirt', 
        description='test shirt desc', price=30)

    def test_product_list_view(self):
        response = self.client.get(reverse('core:product_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/product_list.html')

    def test_product_list_by_category_view(self):
        response = self.client.get(reverse('core:product_list_by_category', kwargs={"category_slug": "pants"}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/product_list.html')

    def test_product_detail_view(self):
        response = self.client.get(reverse('core:product_detail', kwargs={'id': 10, 'slug': 'testshirt'}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/product_detail.html')

    def test_product_detail_view_error(self):
        response = self.client.get(reverse('core:product_detail', kwargs={'id': 2, 'slug': 'pants'}))
        self.assertEquals(response.status_code, 404)

