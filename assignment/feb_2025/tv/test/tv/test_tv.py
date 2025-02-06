from unittest import TestCase

from tv.tv import TV, StateException


class MyTestCase(TestCase):
    def setUp(self):
        self.tv = TV()

    def test_tv_can_be_created(self):
        self.assertIsNotNone(self.tv)
        self.assertFalse(self.tv.is_on)
        self.assertEqual(0, self.tv.volume_level)
        self.assertEqual(0, self.tv.channel_level)

    def test_tv_can_be_toggled_on_and_off(self):
        self.assertFalse(self.tv.is_on)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on)

    def test_tv_volume_can_be_increased_only_when_turned_on(self):
        self.assertFalse(self.tv.is_on)
        self.assertRaises(StateException, self.tv.increase_volume)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.assertEqual(0, self.tv.volume_level)
        self.tv.increase_volume()
        self.assertEqual(1, self.tv.volume_level)
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.assertEqual(3, self.tv.volume_level)


    def test_tv_volume_can_not_increase_beyond_100_percent(self):
        self.assertEqual(0, self.tv.volume_level)
        for i in range(150):
            self.tv.increase_volume()
        self.assertEqual(100, self.tv.volume_level)

