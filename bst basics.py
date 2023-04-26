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
#Max with recursion    
  def maxR(self, root):
    if root is None:
      return None
    elif root.right_child is None:
      return root.data
    else:
      return self.maxR(root.right_child)
#Max with iteration  
  def max(self):
    if self.root is None:
      return None
    current=self.root
    while current.right_child is not None:
      current=current.right_child
    return current.data
#Min with recursion
  def minR(self, root):
    if root is None:
      return None
    elif root.left_child is None:
      return root.data
    else:
      return self.minR(root.left_child)
#Min with iteration
  def min(self):
    if self.root is None:
      return None
    current=self.root
    while current.left_child is not None:
      current=current.left_child
    return current.data
#search with iteration
  def search(self, data):
    if self.root is None:
      return False

    current=self.root
    while current:
      if data==current.data:
        return True
      elif data<current.data:
        current=current.left_child
      else:
        current=current.right_child
    return False
#Search with recursion
  def searchR(self, root, data):
    if root is None:
      return False
    else:
      if data==root.data:
        return True
      elif data<root.data:
        return self.searchR(root.left_child, data)
      else:
        return self.searchR(root.right_child, data)
    



bst=BinarySearchTree()
list_bst=[20, 60, 85, 70, 16, 18, 19, 17, 5]
for i in list_bst:
  bst.root=bst.insertR(bst.root, i)

print('in-order')
bst.print_in()

print('Max:',bst.max())

print('Min',bst.min())

print('Searched data:',bst.searchR(bst.root, 20))
