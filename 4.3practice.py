class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data  = data
        self.left  = left
        self.right = right
        self.depth = None

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        new_node = ListNode(node)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '->'.join(nodes)

class Queue:
    def __init__(self):
        self.array = []

    def add(self, item=None):
        if not item:
            return None
        return self.array.append(item)

    def remove(self):
        if not self.array:
            return None
        return self.array.pop(0)

def list_of_depths(root):
    if not root:
        return "Bad entry"
    lists = []
    current_depth = -1
    node = root
    node.depth = 0
    queue = Queue()
    while node:
        # Add to linked list
        if node.depth == current_depth:
            linkedlist.insert(node.data)
        else:
            current_depth = node.depth
            linkedlist = LinkedList()
            linkedlist.insert(node.data)
            lists.append(linkedlist)
        # Add to queue
        for child in [node.left, node.right]:
            if child:
                child.depth = node.depth + 1
                queue.add(child)
        node = queue.remove()
    return lists


node_h = TreeNode('H')
node_g = TreeNode('G')
node_f = TreeNode('F')
node_e = TreeNode('E', node_g)
node_d = TreeNode('D', node_h)
node_c = TreeNode('C', None, node_f)
node_b = TreeNode('B', node_d, node_e)
node_a = TreeNode('A', node_b, node_c)

print(list_of_depths(node_a))
