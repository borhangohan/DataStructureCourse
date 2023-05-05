#bst
import collections
class Node:
  def __init__(self, data):
    self.data = data
    self.right_child = None
    self.left_child = None
    self.numOfdescendants

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
    
#identical or not
  def indenticalORnot(self, root1, root2):
    if root1 is None and root2 is None:
      return True
    
    elif root1 is None and root2 is not None:
      return False
    elif root1 is not None and root2 is None:
      return False
    else:
      return root1.data==root2.data and self.indenticalORnot(root1.left_child, root2.left_child) and self.indenticalORnot(root1.right_child, root2.right_child)
#count descendants
  def count_descendantsR(self, root):
    if root is None:
      return 0
    else:
      leftCount=self.count_descendantsR(root.left_child)
      rightCount=self.count_descendantsR(root.right_child)
      root.numOfDescendants=leftCount + rightCount
    return root.numOfDescendants + 1  
#count nodes 
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
#leaf node even odds
  def leafnode_evenodd(self, root):
    if root is None:
      return []
    
    elif root.left_child is None and root.right_child is None:
      return [root.data]
    else:
      return self.leafnode_evenodd(root.left_child) + self.leafnode_evenodd(root.right_child)

#max in each level
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

#print nodes
  def print_all_levels(self, root):
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
      final_list.append(temp_list)
    return final_list

  def calculate_sum(self, root):
    current=root
    sum=0
    stack=[]
    while True:
      if current is not None:
        stack.append(current)
        current=current.left_child
      elif stack:
        current=stack.pop()
        sum+=current.data
        current=current.right_child
      else:
        break
    return sum


#sum of all nodes with recursion
  def calculate_sumR(self, root):
    if root is None:
      return 0

    else:
      return root.data + self.calculate_sumR(root.left_child) + self.calculate_sumR(root.right_child)

#bst or not
  def find_min(root):
    current = root
    while current.left_child:
      current = current.left_child
    return current
  
  # Find the node with the maximum value
  def find_max(self, root):
    current = root
    while current.right_child:
      current = current.right_child
    return current
#Recursive
  def isBST(self, root):
     if (root == None):
        return True
     
     if (root.left_child != None and self.find_max(root.left_child).data > root.data ):
        return False
 
     if (root.right_child != None and self.find_min(root.right_child).data < root.data):
        return False
 
     return  (self.isBST(root.left_child) and self.isBST(root.right_child))
        
#Iterative
  def isBSTiter(self, root):

    Stack = []
    prev = None
 
    while (Stack or root):
         while root:
            Stack.append(root)
            root = root.left_child
         root = Stack.pop()
 
         if (prev and root.data <= prev.data):
            return False
   
         prev = root
         root = root.right_child
 
    return True

bst=BinarySearchTree()
list_bst=[20, 60, 85, 70, 16, 18, 19, 17, 5]
for i in list_bst:
  bst.root=bst.insertR(bst.root, i)

print('in-order')
bst.print_in()

print('Max:',bst.max())

print('Min',bst.min())

print('Searched data:',bst.searchR(bst.root, 20))

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
print(bst.count_descendantsR(bst.root)-1)
print(bst.count_nodes(bst.root))
print(bst.count_nodesR(bst.root))
leaf_nodes=bst.leafnode_evenodd(bst.root)
for i in leaf_nodes:
  if i%2==0:
    print(['Even'], end=',')
  else:
    print(['odd'],end=',')
nodes_list=bst.max_each_level(bst.root)
for data in nodes_list:
  print(data)
nodes_list=bst.print_all_levels(bst.root)
for data in nodes_list:
  print(data)