#identical or not

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

  def indenticalORnot(self, root1, root2):
    if root1 is None and root2 is None:
      return True
    
    elif root1 is None and root2 is not None:
      return False
    elif root1 is not None and root2 is None:
      return False
    else:
      return root1.data==root2.data and self.indenticalORnot(root1.left_child, root2.left_child) and self.indenticalORnot(root1.right_child, root2.right_child)
    
bst1=BinarySearchTree()
bst2=BinarySearchTree()
ls1=[25,30,32,31,26,20,22,23,13]
for i in ls1:
  bst1.root=bst1.insertR(bst1.root, i)
ls2=[25,30,32,31,26,20,22,23,13]
for i in ls2:
  bst2.root=bst2.insertR(bst2.root, i)

#bst.inorderR(bst.root)

print(bst1.indenticalORnot(bst1.root, bst2.root))