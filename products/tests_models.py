from django.test import TestCase
from .models import Product, Category


class TestServiceModel(TestCase):

    def test_product_is_properly_created(self):
        product = Product.objects.create(name="Helmet",
                                         description="Test description",
                                         price=9.99)
        self.assertEquals(product.name, "Helmet")
        self.assertEqual(product.price, 9.99)

    def test_category_default_to_true(self):
        category = Category.objects.create(name="New Category")
        self.assertEquals(category.name, "New Category")

    def test_category_is_properly_assigned_to_a_product(self):
        category = Category.objects.create(name="New Category")
        product = Product.objects.create(name="Helmet",
                                         description="Test description",
                                         price=9.99,
                                         category=category)

        self.assertEquals(product.category.name, "New Category")
