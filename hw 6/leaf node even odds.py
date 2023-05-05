#leaf node even odds

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

  def leafnode_evenodd(self, root):
    if root is None:
      return []
    
    elif root.left_child is None and root.right_child is None:
      return [root.data]
    else:
      return self.leafnode_evenodd(root.left_child) + self.leafnode_evenodd(root.right_child)
    
      

bst=BinarySearchTree()
ls=[25,30,32,31,26,20,22,23,13]
for i in ls:
  bst.root=bst.insertR(bst.root, i)
#for data in range(0,len(ls)):
 # bst.insert(ls[data])

print('          25         ')
print('        /    \       ')
print('      20     30      ')
print('     /  \   /  \     ')
print('    13  22 26  32    ')
print('         \     /     ')
print('         23   31     ')

#bst.inorderR(bst.root)
#print('')
print('leaf nodes:')
print(bst.leafnode_evenodd(bst.root))
leaf_nodes=bst.leafnode_evenodd(bst.root)
for i in leaf_nodes:
  if i%2==0:
    print(['Even'], end=',')
  else:
    print(['odd'],end=',')