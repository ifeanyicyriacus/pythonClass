class StateException(Exception):
    def __init__(self, msg):
        super(StateException, self).__init__(msg)


class TV:
    def __init__(self):
        self._is_on = False
        self._volume_level = 0
        self._channel_level = 0

    @property
    def is_on(self):
        return self._is_on
    @is_on.setter
    def is_on(self, value:bool) -> None:
        self._is_on = value

    @property
    def volume_level(self):
        return self._volume_level
    @volume_level.setter
    def volume_level(self, value:int) -> None:
        self._volume_level = value

    @property
    def channel_level(self):
        return self._channel_level

    @channel_level.setter
    def channel_level(self, value:int) -> None:
        self._channel_level = value

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def increase_volume(self):
        if not self._is_on:
            raise StateException('TV is not turned on')
        # raise warning alert
        if self.volume_level < 100:
            self.volume_level += 1
