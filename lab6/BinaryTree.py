from typing import Any, Callable
from BinaryNode import BinaryNode


class BinaryTree:

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    def traverse_in_order(self,visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self,visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)
