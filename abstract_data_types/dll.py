# Big O notation: O(1) for add_front, O(n) for size, search, and remove

import dataclasses
import typing

@dataclasses.dataclass
class DLLNode:
    """ Node for Doubly Linked list """

    data: typing.Any
    next: typing.Self | None = None
    previous: typing.Self | None = None

    def __repr__(self) -> str:
        return f"DLLNode object: {self.data}"

    def get_data(self):
        return self.data

    def set_data(self, new_data) -> None:
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next) -> None:
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous) -> None:
        self.previous = new_previous


@dataclasses.dataclass
class DLL:
    """ Doubly Linked list """

    head: DLLNode | None

    def __repr__(self) -> str:
        return f"DLL object: {self.head}"

    def is_empty(self) -> bool:
        return self.head is None

    def add_front(self, new_data) -> None:
        temp = DLLNode(data=new_data)
        temp.set_next(new_next=self.head)

        if self.head:
            self.head.set_previous(new_previous=temp)

        self.head = temp

    def size(self) -> int:
        """ O(n) """
        size: int = 0
        if self.head is None:
            return size
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def search(self, data) -> DLLNode | str:
        if self.head is None:
            return "Linked List is empty"

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        return "A Node with that data value is not present."

    def remove(self, data) -> str | None:
        """ O(n) """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()
        if current.previous is None:
            self.head: DLLNode = current.get_next()
        else:
            current.previous.set_next(new_next=current.get_next())
            current.next.set_previous(new_previous=current.get_previous())
        return None


my_dll = DLL(DLLNode(data="first", next=None, previous=None))
my_dll.add_front(new_data="second")
my_dll.add_front(new_data="third")
print(my_dll.search("second"))
print(my_dll.search("fourth"))
print(my_dll.size())

# Iterate through the list and print each node
next_node = my_dll.head
while next_node is not None:
    print(next_node)
    next_node = next_node.get_next()
