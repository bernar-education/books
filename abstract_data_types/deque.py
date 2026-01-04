import dataclasses


@dataclasses.dataclass
class Deque:
    """ Abstract Data Type Deque """

    items: list = dataclasses.field(default_factory=list)

    def add_front(self, item) -> None:
        self.items.insert(0, item)

    def add_rear(self, item) -> None:
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    @property
    def size(self) -> int:
        return len(self.items)

    @property
    def is_empty(self) -> bool:
        return self.items == []


my_deque = Deque()
my_deque.add_front("apple")
my_deque.add_front("strawberry")
my_deque.add_front("orange")
my_deque.add_rear("banana")
print(my_deque.items)