# Big O notation: O(1) for push/pop/peek operations

import dataclasses


@dataclasses.dataclass
class Stack:
    """ Abstract Data Type Stack """

    items: list = dataclasses.field(default_factory=list)

    def push(self, item) -> None:
        self.items.append(item)

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    @property
    def size(self) -> int:
        return len(self.items)

    @property
    def is_empty(self) -> bool:
        return self.items == []