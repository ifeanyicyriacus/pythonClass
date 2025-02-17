
class InfiniteCollection:
    def __init__(self, capacity):
        self.__size = 0
        self.__capacity = capacity
        self.__collection = []

    @property
    def size(self) -> int:
        return self.__size

    @property
    def is_empty(self) -> bool:
        return self.__size == 0

    @property
    def is_full(self) -> bool:
        return self.__size == self.__capacity

    @property
    def collection(self) -> list:
        return self.__collection

    @collection.setter
    def collection(self, collection):
        self.__collection = collection

    def contains(self, item: object) -> bool:
        for element in self.__collection:
            if element == item:
                return True
        return False

    def clear(self):
        self.__collection = []
        self.__size = 0

    def count(self, item: object) -> int:
        count = 0
        for element in self.__collection:
            if element == item:
                count += 1
        return count