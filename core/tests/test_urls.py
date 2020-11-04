from core.views import *
from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

    def test_list_url(self):
        url = reverse('core:product_list')
        self.assertEquals(resolve(url).func, product_list)

    def test_list_by_category_url(self):
        url = reverse('core:product_list_by_category', args=['jeans'])
        self.assertEquals(resolve(url).func, product_list)

    def test_detail_url(self):
        url = reverse('core:product_detail', kwargs={'id': 2, 'slug': 'pants'})
        self.assertEquals(resolve(url).func, product_detail)
