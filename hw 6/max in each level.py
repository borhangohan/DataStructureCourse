#max in each level
import collections
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

  def max_each_level(self, root):
    final_list=[]
    if root is None:
      return final_list
    
    queue=collections.deque()
    queue.append(root)

    while queue:
      temp_list=[]
      queue_size=len(queue)
      
      while queue_size>0:
        temp_node=queue.popleft()
        temp_list.append(temp_node.data)
        queue_size-=1
        
        if temp_node.left_child is not None:
          queue.append(temp_node.left_child)
        
        if temp_node.right_child is not None:
          queue.append(temp_node.right_child)      
      final_list.append(max(temp_list))
    return final_list

bst=BinarySearchTree()
ls=[25,30,32,31,26,20,22,23,13]
for i in ls:
  bst.root=bst.insertR(bst.root, i)
#for data in range(0,len(ls)):
 # bst.insert(ls[data])

bst.inorderR(bst.root)
print('\r')
print('Max in each node:')
nodes_list=bst.max_each_level(bst.root)
for data in nodes_list:
  print(data)
