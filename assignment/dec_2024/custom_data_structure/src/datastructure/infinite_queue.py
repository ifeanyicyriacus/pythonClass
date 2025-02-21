
from datastructure.infinite_collection import InfiniteCollection


# class IllegalStateException(Exception):
#     def __init__(self, message):
#         super().__init__(message)

class InfiniteQueue(InfiniteCollection):
    __pointer: int = 0
    __count: int = 0

    def __init__(self, capacity: int):
        super().__init__(capacity)

    @property
    def is_full(self) -> bool:
        return self.size == self.__capacity

    @property
    def is_empty(self) -> bool:
        for item in self.collection:
            if item is not None:
                return False
        return True

    @property
    def size(self) -> int:
        return self.__count

    @size.setter
    def size(self, size: int) -> None:
        self.__count = size

    def add(self, element: object) -> None:
        if self.is_full:
            raise Exception("Queue is full: element cannot be added at this time due to capacity " +
                    "restrictions")
        else:
            self.collection[self.size % self.capacity] = element
            self.size += 1


    def peek(self) -> object:
        return self.collection[self.size % self.capacity]

    def remove(self) -> object:
        if not self.is_empty:
            element = self.peek()
            self.collection[self.size % self.capacity] = None
            self.__pointer += 1
            self.__count -= 1
            return element
        else:
            return None