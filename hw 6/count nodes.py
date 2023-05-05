#count nodes 

class Node:
  def __init__(self, data):
    self.data = data
    self.right_child = None
    self.left_child = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
#Insert with iteration
  def insert(self, newdata):
    newnode=Node(newdata)
    if self.root is None:
      self.root=newnode
    else:
      current=self.root
      parent=None
      while current:
        parent=current
        if newnode.data<=current.data:
          current=current.left_child
        else:
          current=current.right_child
      if newnode.data<=parent.data:
        parent.left_child=newnode
      else:
        parent.right_child=newnode
#Insert with recursion  
  def insertR(self, root, newdata):
    if root is None:
      return Node(newdata)
    else:
      current=root
      if newdata<=current.data:
        current.left_child=self.insertR(current.left_child, newdata)
      else:
        current.right_child=self.insertR(current.right_child, newdata)
    return current
#Inorder print    
  def inorderR(self, root):
    current=root
    if current is None:
      return
    else:
      self.inorderR(current.left_child)
      print(current.data)
      self.inorderR(current.right_child)
  
  def print_in(self):
    self.inorderR(self.root)
  
  def count_nodes(self, root):
    stack=[]
    current=root
    count=0
    while True:
      if current is not None:
        stack.append(current)
        current=current.left_child
      elif stack:
        current=stack.pop()
        count+=1
        current=current.right_child
      else:
        break
    return count
  
  def count_nodesR(self, root):
    if root is None:
      return 0
    else:
      return 1 + self.count_nodesR(root.left_child) + self.count_nodesR(root.right_child)
bst=BinarySearchTree()

ls=[25,30,32,31,26,20,22,23,13]
for i in ls:
  bst.root=bst.insertR(bst.root, i)
bst.inorderR(bst.root)
print()
print(bst.count_nodes(bst.root))
print(bst.count_nodesR(bst.root))

