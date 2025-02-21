
from datastructure.infinite_collection import InfiniteCollection


class InfiniteStack(InfiniteCollection):
    def __init__(self, capacity: int):
        super().__init__(capacity)

    def push(self, element: object):
        if self.is_full:
            raise Exception("Stack is full")
        else:
            self.collection[self.size] = element

    def pop(self):
        result = None
        if not self.is_empty:
            result = self.collection[self.size -1]
            self.collection[self.size-1] = None
            self.size -= 1
        return result

    def peek(self):
        return self.collection[self.size-1]

