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
            nodes.append(curr)
            curr = curr.next
        return str(nodes)

    def insert(self, data):
        self.head = Node(data=data, next=self.head)

l = LinkedList()
lst = [1, 2, 3, 4, 8, 1, 2, 2, 'X','X', 3, 4, 3, 2, 8]
for i in reversed(lst):
    l.insert(i)

# solved with temporary buffer
def remove_dups(linkedlist):
    all = []
    prev = None
    curr = linkedlist.head
    while curr:
        if curr.data in all:
            prev.next = curr.next
            curr = curr.next
        else:
            all.append(curr.data)
            prev = curr
            curr = curr.next
    print("final   " + str(linkedlist))

# solved without temporary buffer and two pointers
def remove_dups_no_buffer(linkedlist):
    curr = linkedlist.head
    while curr:
        runner = curr
        while runner.next:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    print("final 2 " + str(linkedlist))

remove_dups(l)
remove_dups_no_buffer(l)
