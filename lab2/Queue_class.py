from List_class import LinkedList, Any


class Queue:
    def __init__(self):
            self.storage = LinkedList()

    def peek(self):
        return self.storage.head.data

    def enqueue(self, element: Any):
        self.storage.append(element)

    def dequeue(self):
        self.storage.pop()

    def print(self):
        temp = self.storage.head
        while (temp):
            if temp.next is None:
                 print(temp.data)
            else:
                print(temp.data, ", ", end="")
            temp = temp.next