class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Stack:
    def __init__(self, top=None, mini=None):
        self.top = top
        self.mini = mini

    def minimum(self):
        if not self.mini:
            return "No minimum value"
        return self.mini.data

    def push(self, item):
        if self.mini and self.mini.data < item:
            self.mini = Node(data=self.mini.data, next=self.mini)
        else:
            self.mini = Node(data=item, next=self.mini)
        self.top = Node(data=item, next=self.top)

    def pop(self):
        if not self.top:
            return "Empty Stack"
        self.mini = self.mini.next
        top = self.top
        self.top = self.top.next
        return repr(top)

    def peek(self):
        if not self.top:
            return "Empty Stack"
        return repr(self.top)

s = Stack()
s.push(24)
s.push(3)
s.push(1)
s.push(32)
s.push(-2)
s.push(8)
# s.pop()
# s.pop()
print(s.peek(), s.minimum())
