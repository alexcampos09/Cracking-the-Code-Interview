class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            print(curr.data)
            nodes.append(repr(curr))
            curr = curr.next
        return ' -> '.join(nodes)

    def loop(self):
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
        prev.next = self.head

l = LinkedList()
l.insert(9)
l.insert(8)
l.insert(7)
l.insert(6)
l.loop()
l.insert(5)
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(1)

def findLoop(l):
    nodes = []
    curr = l.head
    while curr:
        if curr in nodes:
            return "Loop at node " + repr(curr)
        nodes.append(curr)
        curr = curr.next
    return "No loop"

print(findLoop(l))
