class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return(self.next)

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '->'.join(nodes)

    # def del_middle_node(self, data):
    #     print(data.next)

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

lst = LinkedList()
lst.insert(1)
lst.insert(2)
lst.insert(3)
lst.insert(4)
# print(lst)
lst.del_middle_node(Node(3))
# print(lst)
