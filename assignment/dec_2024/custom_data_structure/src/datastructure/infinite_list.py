from datastructure.infinite_collection import InfiniteCollection


class InfiniteList(InfiniteCollection):
    def __init__(self, capacity:int = 0):
        super().__init__(capacity)

    def remove(self, element:object) -> None:
        element_index = self.index_of(element)
        self.collection = (
                self.collection[:element_index]
                + self.collection[element_index + 1:])

    def insert(self, index:int, element:object) -> None:
        if not self.is_full:
            i = index
            while i < self.size:
                temp = self.collection[i]
                self.collection[i] = element
                element = temp
                i += 1

    def index_of(self, element:object) -> int:
        for index in range(self.size):
            if element == self.collection[index]:
                return index
        return -1

    def get(self, index:int) -> object:
        return self.collection[index]

