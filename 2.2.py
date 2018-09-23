class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return str(nodes)

    def insert(self, data):
        self.head = Node(data=data, next=self.head)

lst = SinglyLinkedList()
for i in reversed(range(1, 100)):
    lst.insert(i)

def get_kth(ll, kth):
    count = 0
    curr = ll.head
    while curr:
        count += 1
        curr = curr.next
    idx = count - kth
    curr = ll.head
    while idx != 0:
        curr = curr.next
        idx -= 1
    return curr.data

print(get_kth(lst, 2))
