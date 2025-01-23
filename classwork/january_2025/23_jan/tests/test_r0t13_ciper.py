from unittest import TestCase
from src.r0t13_ciper import encrypt_text

class TestEncryptTextFunction(TestCase):
    def test_encrypt_text_exist(self):
        self.assertEqual("", encrypt_text(""))

    def test_encrypt_text_return_encrypted_text(self):
        text = "Hello, World!"
        expected_text = "Uryyb, Jbeyq!"
        actual_text = encrypt_text(text)
        self.assertEqual(expected_text, actual_text)
