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

    def findMaxR(self, root):
        if root is None:
            return None
        
        if root.right is None:
            return root.data
        
        return self.findMaxR(root.right)
    
    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)

    def print(self):
        self.print_in_order(self.root)

bst = BST()
bst.insertR(5)
bst.insertR(3)
bst.insertR(7)
bst.insertR(1)
bst.insertR(4)
bst.insertR(6)
bst.insertR(8)

max_val = bst.findMaxR(bst.root)
print(max_val)  # output: 8



