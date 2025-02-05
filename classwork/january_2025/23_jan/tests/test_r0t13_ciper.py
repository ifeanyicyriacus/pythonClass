from unittest import TestCase
from src.r0t13_ciper import encrypt_text, decrypt_text

class TestEncryptTextFunction(TestCase):
    def test_encrypt_text_exist(self):
        self.assertEqual("", encrypt_text(""))

    def test_encrypt_text_return_encrypted_text(self):
        text = "Hello, World!"
        expected_text = "Uryyb, Jbeyq!"
        actual_text = encrypt_text(text)
        self.assertEqual(expected_text, actual_text)

        text = "Good morning, Nigeria! what is the 411"
        expected_text = "Tbbq zbeavat, Avtrevn! jung vf gur 411"
        actual_text = encrypt_text(text)
        self.assertEqual(expected_text, actual_text)

    def test_encrypt_text_return_does_not_encrypt_non_alphabet_letters(self):
        text = "34, 123!"
        actual_text = encrypt_text(text)
        self.assertEqual(text, actual_text)

class TestDecryptTextFunction(TestCase):
    def test_decrypt_text_return_decrypted_text(self):
        text = "Uryyb, Jbeyq!"
        expected_text = "Hello, World!"
        actual_text = decrypt_text(text)
        self.assertEqual(expected_text, actual_text)

        text = "Tbbq zbeavat, Avtrevn! jung vf gur 411"
        expected_text = "Good morning, Nigeria! what is the 411"
        actual_text = decrypt_text(text)
        self.assertEqual(expected_text, actual_text)