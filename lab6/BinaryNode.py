from typing import Any, Callable


class BinaryNode:
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.right_child = None
        self.left_child = None

    def is_leaf(self) -> bool:
        if self.left_child or self.right_child:
            return False
        else:
            return True

    def add_left_child(self, dziecko: Any):
        self.left_child = BinaryNode(dziecko)

    def add_right_child(self, dziecko: Any):
        self.right_child = BinaryNode(dziecko)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self,visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self,visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def __str__(self) -> str:
        return str(self.value)



