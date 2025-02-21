from datastructure.infinite_list import InfiniteList
from datastructure.infinite_set import InfiniteSet


class InfiniteMap:
    def __init__(self):
        self.__keys = InfiniteSet()
        self.__values = InfiniteList()

    @property
    def is_empty(self):
        return self.keys.is_empty and self.values.is_empty

    @property
    def capacity(self):
        return self.keys.capacity

    @property
    def size(self):
        return self.keys.size

    def add(self, key:object, value:object):
        if key in self.keys:
            index:int = self.keys.index_of(key)
            self.values.replace(index, value)
        else:
            self.keys.add(key)
            self.values.add(value)

    def get(self, key:int):
        index:int = self.keys.index_of(key)
        if index != -1:
            return self.values.get(index)
        return None
    @property
    def keys(self):
        return self.__keys

    @property
    def values(self):
        return self.__values

    def remove(self, key:object):
        index:int = self.keys.index_of(key)
        if index != -1:
            self.keys.remove(index)
            self.values.remove(index)
    @property
    def items(self) -> tuple:
        return self.keys, self.values

    def __str__(self):
        result:str = "{\n"
        for key, value in self.items:
            result += "\t"
            result += f'"{key}": {value},\n'
        result:str = "}\n"
        return result

