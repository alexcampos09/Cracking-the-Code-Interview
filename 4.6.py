class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

def successor(node):
    if not node:
        return None
    child = node.right
    if child:
        while child.left:
            child = child.left
    if child:
        return child
    if node.parent:
        while node.parent:
            if node.parent.data > node.data:
                return node.parent
            node.parent = node.parent.parent
    return None

MegaTree = Node(10,
            Node(5,
                Node(3,
                    None,
                    Node(4)),
                Node(8,
                    Node(7),
                    Node(9))),
            Node(11,
                None,
                Node(15,
                    Node(14),
                    Node(16))))

import unittest

class Test(unittest.TestCase):
  def test_successor(self):
    self.assertEqual(successor(Node(22, Node(11))), None)
    self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
    self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)
    self.assertEqual(successor(MegaTree.left.right.right).data, 10)

if __name__ == "__main__":
  unittest.main()
