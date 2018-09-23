class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def binaryTreeToList(binary_tree, l=[]):
    if not binary_tree:
        return None
    binaryTreeToList(binary_tree.left)
    l.append(binary_tree.data)
    binaryTreeToList(binary_tree.right)
    return l

tree = Node(5, Node(3, Node(1, None, Node(2)), Node(4)), Node(7, Node(6), Node(8)))
print(binaryTreeToList(tree))
