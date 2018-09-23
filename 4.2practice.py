class Node:
    def __init__(self, data, left=None, right=None):
        self.data  = data
        self.left  = left
        self.right = right

    def __repr__(self):
        string = "(" + str(self.data)
        if self.left:
            string += str(self.left)
        else:
            string += "."
        if self.right:
            string += str(self.right)
        else:
            string += "."
        return string + ")"

def binarySearchTree(sorted_array):
    print(sorted_array)
    if not sorted_array:
        return None
    middle = len(sorted_array)/2
    left = binarySearchTree(sorted_array[:middle])
    right = binarySearchTree(sorted_array[(middle+1):])
    return Node(sorted_array[middle], left, right)

l = []
for i in range(5):
    l.append(i)
print(binarySearchTree(l))
