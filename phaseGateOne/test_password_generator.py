from unittest import TestCase
from password_generator import generate_password, allCharacterTypeAreRepresentedIn

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = lower_alphabet.upper()
numbers = "0123456789"
symbols = "`~!@#$%^&*()_-+=\\|}][{'\":;/?>.,<"
character_groups = [lower_alphabet, upper_alphabet, numbers, symbols]

class TestGeneratePasswordFunction(TestCase):
    def test_that_generate_password_exists(self):
        generate_password()
    
    def allCharacterTypeAreRepresentedIn(self, password:str, character_groups:list) -> bool:
        password_list = password.replace("", " ").strip().split(" ")
        
        for character_group in character_groups:
            if all([character not in character_group for character in password_list]):
                return False
        return True

    def test_that_generate_password_return_correct_value(self):
        password = generate_password()
        for _ in range(100000):
            self.assertTrue(self.allCharacterTypeAreRepresentedIn(password, character_groups))
    
