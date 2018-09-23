class MyQueue:
    def __init__(self):
        self.original = []
        self.secondary = []

    def push(self, data):
        if not self.original and self.checkQueue:
            self.changeStack()
        self.original.append(data)

    def changeStack(self):
        if len(self.original) < len(self.secondary):
            source, receptor = self.secondary, self.original
        else:
            source, receptor = self.original, self.secondary
        while len(source) > 0:
            receptor.append(source.pop())

    def peek(self):
        if not self.checkQueue():
            print("Queue is empty")
            return
        if not self.secondary:
            self.changeStack()
        print(self.secondary[-1])

    def pop(self):
        if not self.checkQueue():
            print("Queue is empty")
            return
        if not self.secondary:
            self.changeStack()
        return self.secondary.pop()

    def checkQueue(self):
        # print(self.original, self.secondary)
        if not self.original and not self.secondary:
            return False
        return True

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.peek()
q.pop()
q.peek()
q.pop()
q.peek()
q.pop()
q.peek()
q.push(6)
q.push(7)
q.push(8)
q.push(9)
q.pop()
q.peek()
q.pop()
q.peek()
q.pop()
q.peek()
q.pop()
q.peek()
q.pop()
q.peek()
q.pop()
q.peek()
q.peek()
q.peek()
q.peek()
q.peek()
