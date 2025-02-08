
class StateException(Exception):
    def __init__(self, msg):
        super(StateException, self).__init__(msg)


class TV:
    MAX_VOLUME: int = 100
    MIN_VOLUME: int = 0
    MAX_CHANNEL: int = 100
    MIN_CHANNEL: int = 0

    def __init__(self):
        self.__tempVolume:int = 0
        self.__is_on = False
        self.__volume_level = self.MIN_VOLUME
        self.__channel_level = self.MIN_CHANNEL

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, value: bool) -> None:
        self.__is_on = value

    @property
    def volume_level(self):
        return self.__volume_level

    @volume_level.setter
    def volume_level(self, value: int) -> None:
        self.__volume_level = value

    @property
    def channel_level(self):
        return self.__channel_level

    @channel_level.setter
    def channel_level(self, value: int) -> None:
        self.__channel_level = value

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def increase_volume(self):
        self.__power_on_check()
        if self.volume_level < self.MAX_VOLUME:
            self.volume_level += 1

    def decrease_volume(self):
        self.__power_on_check()
        if self.volume_level > self.MIN_VOLUME:
            self.volume_level -= 1

    def channel_up(self):
        self.__power_on_check()
        if self.channel_level < self.MAX_CHANNEL:
            self.channel_level += 1

    def channel_down(self):
        self.__power_on_check()
        if self.channel_level > self.MIN_CHANNEL:
            self.channel_level -= 1

    def set_channel(self, channel_level):
        self.__power_on_check()
        if self.MIN_CHANNEL <= channel_level <= self.MAX_CHANNEL:
            self.channel_level = channel_level
            return
        raise ValueError('invalid channel level Entered')

    def mute(self) -> None:
        self.__power_on_check()
        self.__tempVolume = self.volume_level
        self.volume_level = self.MIN_VOLUME

    def unmute(self):
        self.__power_on_check()
        self.volume_level = self.__tempVolume

    def __power_on_check(self):
        if not self.is_on:
            raise StateException('TV is not turned on')

