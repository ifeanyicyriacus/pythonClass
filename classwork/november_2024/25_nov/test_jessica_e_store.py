from unittest import TestCase
from jessica_e_store import *

class TestRemoveFromCartFunction(TestCase):
    def test_that_remove_from_cart_exist(self):
        remove_from_cart(cart = [])

class TestRemoveFromCartFunction(TestCase):
    def test_that_add_to_cart_exist(self):
        add_to_cart(cart = [], products = [])

class TestViewProductsFunction(TestCase):
    def test_that_view_products_exist(self):
        view_products(products = [])

class TestViewCartFunction(TestCase):
    def test_that_view_cart_exist(self):
        view_cart(cart = [])

class TestCalculateTotalFunction(TestCase):
    def test_that_calculate_total_exist(self):
        calculate_total(cart = [])
    def test_that_calculate_total_return_correct_value(self):
        actual = calculate_total(cart = [["Laptop", 1000], ["Phone", 500], ["Headphones", 100]])  
        expected = 1600
        self.assertEqual(actual, expected)

class TestCheckoutFunction(TestCase):
    def test_that_checkout_exist(self):
        checkout(cart = [])
