from List_class import LinkedList
from Stack_class import Stack
from Queue_class import Queue

def main():
    lista=LinkedList()
    lista.push(7)
    lista.push(1)
    lista.push('sebek')
    lista.insert(4,lista.head)
    lista.append(12)

    lista.print()
    lista.pop()
    lista.remove_last()
    lista.remove(lista.head)
    lista.print()

    stos=Stack()
    stos.push(1)
    stos.push(3)
    stos.push(14)
    stos.pop()
    stos.push(51)
    stos.print()

    kolejka = Queue()
    kolejka.enqueue('klient1')
    kolejka.enqueue('klient2')
    kolejka.enqueue('klient3')
    print(kolejka.peek())
    kolejka.print()
    kolejka.dequeue()
    print(kolejka.peek())
    kolejka.print()


if __name__=="__main__":
    main()