class SortedStack:
    def __init__(self):
        self.main = []
        self.temp = []

    def push(self, data):
        if self.isEmpty() or data < self.peek():
            self.main.append(data)
        else:
            while self.main and data > self.peek():
                self.temp.append(self.main.pop())
            self.main.append(data)
            while self.temp:
                self.main.append(self.temp.pop())

    def peek(self):
        print(self.main)
        return self.main[-1]


    def pop(self):
        if not self.isEmpty():
            return self.main.pop()

    def isEmpty(self):
        if len(self.main) == 0:
            print("Empty Stack")
            return True
        return False

s = SortedStack()
s.push(3)
s.push(2)
s.push(5)
s.push(7)
s.pop()
s.push(1)
s.peek()
s.pop()
s.pop()
s.peek()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
