from django.test import TestCase
from django.utils import timezone
from core.models import Category, Product


class CategoryTest(TestCase):
    
    def create_category(self):
        return Category.objects.create(name="pants")

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.name)


class ProductTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='jeans', slug='jeans')

    def create_product(self):
        return Product.objects.create(category=self.category, name='pejeans', price=500, created=timezone.now(), 
        modified=timezone.now())

    def test_product_creation(self):
        p = self.create_product()
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(p.__str__(), p.name)