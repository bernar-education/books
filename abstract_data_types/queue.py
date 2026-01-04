import dataclasses


@dataclasses.dataclass
class Queue:
    """ Abstract Data Type Queue """

    def __init__(self):
        self.items: list = []

    def enqueue(self, item) -> None:
        """
        The runtime is O(n) or linear time, change index positions
        :param item: Any
        :return: None
        """
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.items == []
