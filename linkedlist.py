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

a=singlylinkedlist()

a.append(1)
a.append(2)
a.append(3)
a.append(4)

a.print()
print()
print(a.search(3))

a.appendleft(2)
a.appendleft(3)
a.appendleft(4)
a.print()
print()

a.pop_left()
a.print()
