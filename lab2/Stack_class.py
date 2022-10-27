from List_class import LinkedList,Any


class Stack:
    def __init__(self):
            self.storage = LinkedList()

    def push(self, element:Any):
        self.storage.push(element)

    def pop(self) -> Any:
        self.storage.pop()

    def print(self):
        temp = self.storage.head
        while (temp):
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data)
            temp = temp.next

    def len(self):
        dlugosc = 0
        temp = self.head
        while (temp):
            dlugosc += 1
            temp = temp.next
        return dlugosc