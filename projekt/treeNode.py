from typing import Any, Callable, Union, List
from graphviz import *


class TreeNode:

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children: List["TreeNode"] = []

    def is_leaf(self) -> bool:
        if self.children:
            return False
        else:
            return True

    def for_each_deep_first(self, visit: Callable[["TreeNode"], None]):
        visit(self)
        for j in self.children:
            j.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[["TreeNode"], None]):
        temp = [self]
        while temp:
            visit(temp[0])
            for i in temp[0].children:
                temp.append(i)
            temp.pop(0)

    def add(self, dziecko: "TreeNode") -> None:
        self.children.append(dziecko)

    def show(self, tree=Graph("drzewo")):
        tree.node(str(self), str(self.value), shape='oval', fontcolor='red',
                  fontname='Comic Sans MS', fontsize='26')
        for j in self.children:
            tree.edge(str(self),str(j))
            j.show(tree)
        return tree

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for j in self.children:
            if j.search(value):
                return j.search(value)
