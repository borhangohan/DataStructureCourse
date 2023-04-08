import random
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insertR(self, data):
        def _insert(node, data):
            if node is None:
                return Node(data)
            
            if data < node.data:
                node.left = _insert(node.left, data)
            else:
                node.right = _insert(node.right, data)
            
            return node
        
        self.root = _insert(self.root, data)
    
    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)

    def print(self):
        self.print_in_order(self.root)

bst = BST()
data = [random.randint(1, 100) for i in range(12)]

for num in data:
    bst.insertR(num)
bst.print()