from datastructure.infinite_list import InfiniteList


class InfiniteSet(InfiniteList):
    def add(self, element:object|list) -> None:
        if type(element) == list:
            for item in element:
                self.add(item)

        if not self.contains(element):
            super().add(element)

    def count(self, element:object) -> int:
        for item in self.collection:
            if item == element: return 1
        return 0
