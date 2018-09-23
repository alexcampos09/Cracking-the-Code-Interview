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

lst = LinkedList()
l = [1, 2, 3, 4, 4, 3, 2, 1]
for i in l:
    lst.insert(i)

def is_palindrome(lst):
    reverse = LinkedList()
    curr = lst.head
    while curr:
        reverse.insert(curr.data)
        curr = curr.next

    curr1, curr2 = lst.head, reverse.head
    while curr1:
        if curr1.data != curr2.data:
            return "Linked List is not a palindrome"
        curr1 = curr1.next
        curr2 = curr2.next
    return "Linked List is a palindrome"

print(is_palindrome(lst))
