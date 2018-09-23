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

    def insertIntersection(self):
        crazyNode = Node('Crazy')
        crazyNode.next = l1.head
        self.head = crazyNode

l1, l2 = LinkedList(), LinkedList()
lst1 = [3, 2, 1, 'L1 here!']
for i in lst1:
    l1.insert(i)
l2.insert('a')
l2.insert(1)
l2.insertIntersection()
l2.insert(2)
l2.insert(3)
l2.insert('b')
l2.insert('c')

print(l1, l2)

def intersection(l1, l2):
    nodes = []
    curr1 = l1.head
    curr2 = l2.head
    while curr1:
        nodes.append(curr1)
        curr1 = curr1.next
    while curr2:
        if curr2 in nodes:
            return 'intersection!'
        # print(curr2, curr2.data)
        curr2 = curr2.next

print(intersection(l1, l2))
