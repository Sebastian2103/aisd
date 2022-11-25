from BinaryTree import BinaryTree
from BinaryNode import BinaryNode


def wypisz(cos: BinaryNode):
    print(cos.value)


def main() -> None:
    binarynode = BinaryNode(10)
    binarynode.add_left_child(9)
    binarynode.left_child.add_left_child(1)
    binarynode.left_child.add_right_child(3)
    binarynode.add_right_child(2)
    binarynode.right_child.add_left_child(4)
    binarynode.right_child.add_right_child(6)
    tree = BinaryTree(binarynode)
    tree.traverse_pre_order(print)

    tree.traverse_in_order(wypisz)


if __name__ == "__main__":
    main()
