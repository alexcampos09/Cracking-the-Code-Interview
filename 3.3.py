class MultiStack:
    def __init__(self, limit):
        self.limit = limit
        self.stacks = []

    def push(self, item):
        if len(self.stacks) and len(self.stacks[-1]) < self.limit:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        if len(self.stacks) == 0:
            print("No Stacks")
            return None
        item = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return item

    def allMightyPeek(self):
        for i in self.stacks:
            print(i)

    def pop_at(self, stackNumber):
        if (stackNumber < 0) or (len(self.stacks) <= stackNumber):
            return None
        if len(self.stacks[stackNumber]) == 0:
            return None
        return self.stacks[stackNumber].pop()

s = MultiStack(2)

for i in range(1, 10):
    s.push(i)

s.push(1)
s.push(2)
s.push(2)
s.pop()
s.pop_at(2)
s.pop_at(2)
s.pop_at(2)

s.allMightyPeek()
