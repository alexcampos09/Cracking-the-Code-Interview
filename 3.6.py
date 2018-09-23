class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, pet):
        new_node = Pet(pet)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return " -> ".join(nodes)

class AnimalShelter(LinkedList):
    def __init__(self):
        super().__init__(head=None)
        self.cats = LinkedList()
        self.dogs = LinkedList()

class Pet:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Cat(Pet): pass
class Dog(Pet): pass

l = AnimalShelter()
l.insert(Dog("Luna"))
l.insert(Dog("Lola"))
l.insert(Dog("Theo"))
l.insert(Dog("Nina"))
l.insert(Cat("Spooky"))
print(l)
