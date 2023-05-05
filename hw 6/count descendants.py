#count descendants

class Node:
  def __init__(self, data):
    self.data = data
    self.right_child = None
    self.left_child = None
    self.numOfDescendants = 0

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
  
  def count_descendantsR(self, root):
    if root is None:
      return 0
    else:
      leftCount=self.count_descendantsR(root.left_child)
      rightCount=self.count_descendantsR(root.right_child)
      root.numOfDescendants=leftCount + rightCount
    return root.numOfDescendants + 1  

bst=BinarySearchTree()

ls=[25,30,32,31,26,20,22,23,13]
for i in ls:
  bst.root=bst.insertR(bst.root, i)
bst.inorderR(bst.root)
print()
print(bst.count_descendantsR(bst.root)-1)

