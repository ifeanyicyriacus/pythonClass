from infinite_list import InfiniteList

class InfiniteArray(InfiniteList):
    def __init__(self, size):
        super().__init__(size)

    def add(self, item:object) -> None:
        if self.is_full:
            self.collection += [item]
        else: raise IndexError("Array capacity reached")

    def add_all(self, items:list) -> None:
        for item in items:
            self.add(item)

    def remove_all(self, items:object) -> None:
        count = self.count(items)
        for _ in range(count):
            self.collection.remove(items)
