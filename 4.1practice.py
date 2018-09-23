class Node:
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list = adjacency_list or []
        #

    def add_edge_to(self, node):
        self.adjacency_list.append(node)

    def __str__(self):
        return self.data

class Queue:
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self):
        if not self.array:
            return None
        return self.array.pop(0)

def find_route(node1, node2):
    node = node1
    queue = Queue()
    visited = []
    while node:
        if node == node2:
            return "There is a route!"
        for adjacent in node.adjacency_list:
            if adjacent not in visited:
                queue.add(adjacent)
        visited.append(node)
        node = queue.remove()
    return "There is no route"


node_j = Node('J')
node_i = Node('I')
node_h = Node('H')
node_d = Node('D')
node_f = Node('F', [node_i])
node_b = Node('B', [node_j])
node_g = Node('G', [node_d, node_h])
node_c = Node('C', [node_g])
node_a = Node('A', [node_b, node_c, node_d])
node_e = Node('E', [node_f, node_a])
node_d.add_edge_to(node_a)

print(find_route(node_a, node_i))
print(find_route(node_a, node_j))

node_h.add_edge_to(node_i)

print(find_route(node_a, node_i))
