from treeNode import TreeNode
from tree import Tree


def wypisz(cos: TreeNode):
    print(cos.value)


def main() -> None:
    a = TreeNode('F')
    a.add(TreeNode('B'))
    a.add(TreeNode('G'))
    a.children[0].add(TreeNode('A'))
    a.children[0].add(TreeNode('D'))
    a.children[0].children[1].add(TreeNode('C'))
    a.children[0].children[0].add(TreeNode('E'))
    a.children[1].add(TreeNode('I'))
    a.children[1].children[0].add(TreeNode('H'))
    a.for_each_deep_first(wypisz)
    print('________________________')
    a.for_each_level_order(wypisz)
    drzewo = Tree(a)
    drzewo.add('N', drzewo.root.search('F'))
    print(a.children[0].children[1].children[0].is_leaf())
    print(drzewo.root.is_leaf())
    drzewo.show()

if __name__ == "__main__":
    main()