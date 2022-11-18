from treeNode import TreeNode
from typing import Any, Callable


class Tree:

    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def for_each_level_order(self, vist: Callable[['TreeNode'],None]) -> None:
        self.root.for_each_level_order(vist)

    def add(self, value: Any, rodzic: TreeNode) -> None:
        rodzic.add(TreeNode(value))

    def for_each_deep_first(self, visit: Callable[['TreeNode'],None]):
        self.root.for_each_deep_first(visit)

    def show(self):
        self.root.show().render(filename='Drzewo', view=True)
