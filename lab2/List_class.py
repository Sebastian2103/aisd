from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def node(self, at: int) -> Node:
        pom = self.head
        for x in range(at):
            pom = pom.next
        return pom

    def insert(self, value: Any, after: Node) -> None:
        if after is None:
            print("Zły Index")
            return

        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def pop(self) -> Any:
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None
            return

    def remove_last(self) -> Any:
        temp = self.head
        while (temp.next):
            prev = temp
            temp = temp.next
        prev.next = None

    def remove(self, after: Node) -> Any:
        if after is None:
            print("Error")
            return
        temp = after.next.next
        after.next = temp

    def print(self):
        temp=self.head
        while(temp):
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data,"-> ", end="")
            temp=temp.next

    def len(self):
        dlugosc=0
        temp=self.head
        while(temp):
            dlugosc+=1
            temp=temp.next
        return dlugosc
