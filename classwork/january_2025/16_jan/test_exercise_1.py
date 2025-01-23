from unittest import TestCase
from country import get_cities_population

class TestCountryPopulationFunction(TestCase):
    def test_country_population_return_correct_value(self):
        valid_country_1 = "USA"
        valid_state_1 = "California"
        valid_country_2 = "Canada"
        valid_state_2 = "Ontario"
        actual = get_cities_population(valid_country_1, valid_state_1)
        expected = ["The population of Los Angeles is 4000000.",
                    "The population of San Francisco is 870000."]
        self.assertEqual(actual, expected)
        actual = get_cities_population(valid_country_2, valid_state_2)
        expected = ["The population of Toronto is 2930000.",
                    "The population of Ottawa is 994837."]
        self.assertEqual(actual, expected)

    def test_country_population_handles_KeyError_By_Sending_error_message(self):
        valid_country = "USA"
        invalid_country = "Niger"
        valid_state = "California"
        invalid_state = "Lagos"
        actual = get_cities_population(invalid_country, valid_state)
        expected = [f"Error: Country Niger not found."]
        self.assertEqual(actual, expected)
        actual = get_cities_population(valid_country, invalid_state)
        expected = [f"Error: State Lagos not in USA."]
        self.assertEqual(actual, expected)

    def test_country_population_returns_(self):
        new_country = "Nigeria"
        new_state = "Lagos"
        actual = get_cities_population(new_country, new_state)
        expected = ["The population of Mainland is 4200329.",
                    "The population of Ikorodu is 4230000."
                    ]
        self.assertEqual(actual, expected)