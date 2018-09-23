class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return ' -> '.join(nodes)

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

lst1, lst2 = LinkedList(), LinkedList()
l1, l2 = [6, 1, 7], [2, 9, 5]
for i in reversed(l1):
    lst1.insert(i)
for i in reversed(l2):
    lst2.insert(i)


def add(l1, l2):
    curr1 = l1.head
    curr2 = l2.head
    n1, n2 = [], []

    while curr1:
        n1.append(repr(curr1))
        curr1 = curr1.next
    while curr2:
        n2.append(repr(curr2))
        curr2 = curr2.next

    n1 = int(''.join(n1))
    n2 = int(''.join(n2))
    return n1 + n2



















print(add(lst1, lst2))
