class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None
        self.size=0

    def append(self, newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newnode
        self.size+=1

    def print(self):
        current=self.head
        while current is not None:
            if current.next is not None:
                print(current.data, end=' => ')
            else:
                print(current.data, end='')
            current=current.next

    def search(self, data):
        current=self.head
        while current is not None:
            if current.data==data:
                return True
            current=current.next
        return False
    
    def appendleft(self, newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.size+=1
    
    def pop_left(self):
        self.head=self.head.next
        self.size-=1
    
    def pop(self):
      current=self.head
      current_node = self.head
      if self.head.next==None:
        self.head = None
      else:
        while current.next is not None:
          if current.next.next==None:
            current.next=None
          else:
            current=current.next
      self.size-=1

    def returnhead(self):
      return self.head.data

    def get_average(self):
      if self.head==None:
        return 'empty'
      sum=0
      count=0
      current=self.head
      while current!=None:
        sum+=current.data
        count+=1
        current=current.next
      average=sum/count
      print(average)
    
    def numofoccurrences(self, head):
      if self.head==None:
        return 0
      count=0
      current=self.head
      while current!=

a=singlylinkedlist()
a.append(5)
a.append(6)
a.append(7)
a.append(8)
a.print()
print()
a.get_average()
