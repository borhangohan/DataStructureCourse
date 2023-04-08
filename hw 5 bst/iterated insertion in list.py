class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        curr_node = self.root
        while True:
            if data < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return
                else:
                    curr_node = curr_node.right

    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)
    
    def print(self):
        self.print_in_order(self.root)

import random

bst = BST()
data = [random.randint(1, 100) for i in range(12)]

for num in data:
    bst.insert(num)

bst.print()
