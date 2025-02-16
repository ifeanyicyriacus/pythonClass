from unittest import TestCase

from src.enums.nigeria_state_and_zone import NigeriaStateGeoPoliticalZones as NgStateGeoPolZones
from src.enums.nigeria_state_and_zone_functions import get_geo_political_zone_by_state

class TestNigeriaStateGeoPoliticalZonesFunctions(TestCase):
    state_1     = "Imo"
    state_2     = "Nasarawa"
    state_3     = "Taraba"
    state_4     = "Kebbi"
    state_5     = "Akwa-Ibom"
    state_6     = "Lagos"
    invalid_state = "New York"

    def test_that_get_geo_political_zone_by_state_function_returns_correct_value(self):
        self.assertEqual(NgStateGeoPolZones.SOUTH_EAST, get_geo_political_zone_by_state(self.state_1))
        self.assertEqual(NgStateGeoPolZones.NORTH_CENTRAL, get_geo_political_zone_by_state(self.state_2))
        self.assertEqual(NgStateGeoPolZones.NORTH_EAST, get_geo_political_zone_by_state(self.state_3))
        self.assertEqual(NgStateGeoPolZones.NORTH_WEST, get_geo_political_zone_by_state(self.state_4))
        self.assertEqual(NgStateGeoPolZones.SOUTH_SOUTH, get_geo_political_zone_by_state(self.state_5))
        self.assertEqual(NgStateGeoPolZones.SOUTH_WEST, get_geo_political_zone_by_state(self.state_6))

    def test_that_get_geo_political_zone_by_state_raises_error_for_invalid_state(self):
        self.assertRaises(ValueError, get_geo_political_zone_by_state, self.invalid_state)

    def test_that_get_geo_political_zone_by_state_returns_human_readable_zones(self):
        self.assertEqual("South-East", str(get_geo_political_zone_by_state(self.state_1)))
        self.assertEqual("North-Central", str(get_geo_political_zone_by_state(self.state_2)))
        self.assertEqual("North-East", str(get_geo_political_zone_by_state(self.state_3)))
        self.assertEqual("North-West", str(get_geo_political_zone_by_state(self.state_4)))
        self.assertEqual("South-South", str(get_geo_political_zone_by_state(self.state_5)))
        self.assertEqual("South-West", str(get_geo_political_zone_by_state(self.state_6)))
