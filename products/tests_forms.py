from django.test import TestCase
from .forms import ProductForm
from .models import Category


class TestProductForms(TestCase):

    def test_create_product_form_complete(self):
        form = ProductForm({
            'name': 'New product',
            'description': 'this is the product i am testing',
            'has_sizes': 'True',
            'rating': 4.5,
            'price': 9.99})
        self.assertTrue(form.is_valid())

    def test_create_product_form_with_invalid_category(self):
        form = ProductForm({
            'name': 'New product',
            'category': 'tt',
            'description': 'This is the description',
            'has_sizes': 'True',
            'rating': 4.5,
            'price': 9.99})
        self.assertFalse(form.is_valid())
        self.assertTrue('category' in form.errors)

    def test_create_product_form_with_a_valid_category(self):
        category = Category({
            'name': 'category_name',
            'friendly_name': 'Helmet'
        })
        form = ProductForm({
            'name': 'New product',
            'category': category.friendly_name,
            'description': 'This is the description',
            'has_sizes': 'True',
            'rating': 4.5,
            'price': 9.99})
        self.assertTrue(form.is_valid())
