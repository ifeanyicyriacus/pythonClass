from unittest import TestCase

from tv.tv import TV, StateException


class MyTestCase(TestCase):
    MAX_VOLUME: int = 100
    MIN_VOLUME: int = 0
    MAX_CHANNEL: int = 100
    MIN_CHANNEL: int = 0
    BELOW_VOLUME_THRESHOLD:int = -1
    ABOVE_VOLUME_THRESHOLD:int = 101

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
        self.tv.turn_on()
        self.assertEqual(0, self.tv.volume_level)
        for i in range(150):
            self.tv.increase_volume()
        self.assertEqual(100, self.tv.volume_level)

    def test_tv_volume_can_be_decrease_only_when_turned_on(self):
        self.tv.turn_on()
        for i in range(10):
            self.tv.increase_volume()
        self.assertEqual(10, self.tv.volume_level)
        self.tv.turn_off()
        self.assertRaises(StateException, self.tv.decrease_volume)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.tv.decrease_volume()
        self.assertEqual(9, self.tv.volume_level)
        self.tv.decrease_volume()
        self.tv.decrease_volume()
        self.assertEqual(7, self.tv.volume_level)

    def test_tv_volume_can_not_decreased_less_than_0_percent(self):
        self.tv.turn_on()
        self.assertEqual(0, self.tv.volume_level)
        for i in range(10):
            self.tv.increase_volume()
        self.assertEqual(10, self.tv.volume_level)

        for i in range(50):
            self.tv.decrease_volume()
        self.assertEqual(0, self.tv.volume_level)

    def test_tv_channel_can_be_increased_only_when_turned_on(self):
        self.assertFalse(self.tv.is_on)
        self.assertRaises(StateException, self.tv.channel_up)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.assertEqual(0, self.tv.channel_level)
        self.tv.channel_up()
        self.assertEqual(1, self.tv.channel_level)
        self.tv.channel_up()
        self.assertEqual(2, self.tv.channel_level)

    def test_tv_channel_can_be_decreased_only_when_turned_on(self):
        self.assertFalse(self.tv.is_on)
        self.assertRaises(StateException, self.tv.channel_down)
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
        self.assertEqual(0, self.tv.channel_level)
        for i in range(10):
            self.tv.channel_up()
        self.assertEqual(10, self.tv.channel_level)
        for i in range(9):
            self.tv.channel_down()
        self.assertEqual(1, self.tv.channel_level)
        self.tv.channel_down()
        self.assertEqual(0, self.tv.channel_level)

    def test_tv_channel_can_not_be_increased_above_100_percent(self):
        self.tv.turn_on()
        self.assertEqual(0, self.tv.channel_level)
        for i in range(150):
            self.tv.channel_up()
        self.assertEqual(100, self.tv.channel_level)

    def test_tv_channel_can_not_be_decreased_below_0_percent(self):
        self.tv.turn_on()
        self.assertEqual(0, self.tv.channel_level)
        for i in range(50):
            self.tv.channel_up()
        self.assertEqual(50, self.tv.channel_level)
        for i in range(100):
            self.tv.channel_down()
        self.assertEqual(0, self.tv.channel_level)

    def test_tv_channel_can_be_set_to_a_specified_number(self):
        self.tv.turn_on()
        self.assertEqual(0, self.tv.channel_level)
        channel_number = 50
        self.tv.set_channel(channel_number)
        self.assertEqual(50, self.tv.channel_level)

    def test_tv_channel_can_only_be_set_if_within_range_0_and_100_percent(self):
        self.tv.turn_on()
        self.tv.set_channel(23)
        self.assertRaises(ValueError, self.tv.set_channel, self.BELOW_VOLUME_THRESHOLD)
        self.assertRaises(ValueError, self.tv.set_channel, self.ABOVE_VOLUME_THRESHOLD)

    def test_tv_sound_can_be_muted(self):
        self.tv.turn_on()
        for i in range(50):
            self.tv.increase_volume()
        self.assertEqual(50, self.tv.volume_level)
        self.tv.mute()
        self.assertEqual(self.MIN_VOLUME, self.tv.volume_level)

    def test_tv_sound_can_be_unmuted(self):
        self.tv.turn_on()
        for i in range(50):
            self.tv.increase_volume()
        self.assertEqual(50, self.tv.volume_level)
        self.tv.mute()
        self.assertEqual(self.MIN_VOLUME, self.tv.volume_level)
        self.tv.unmute()
        self.assertEqual(50, self.tv.volume_level)

