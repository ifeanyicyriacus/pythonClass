from unittest import TestCase
from password_generator import generate_password

class TestGeneratePasswordFunction(TestCase):
    def test_that_generate_password_exists(self):
        generate_password()
