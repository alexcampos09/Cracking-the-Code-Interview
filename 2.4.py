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

    def partition(self, n):
        curr = self.head
        prev = None
        while curr:
            if curr.data < n:
                try:
                    prev.next = curr.next # remove node
                    curr.next = self.head # make curr point to the head
                    self.head = curr
                    curr = prev
                except:
                    pass
            prev = curr
            curr = curr.next
l = [3, 5, 8, 5, 10, 2, 1, 10]
lst = LinkedList()
for i in reversed(l):
    lst.insert(i)
print(lst)
lst.partition(5)
print(lst)
