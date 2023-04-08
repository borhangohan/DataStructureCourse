class node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
    
class dllist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self, newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
        self.size+=1
    def print(self):
        current=self.head
        while current:
            if current.next is None:
                print(current.data, end='')
            else:
                print(current.data, end=' <=> ')
            current=current.next
    
    def inserSorted(self, target):
        newnode=node(target)
        if self.head.data>target:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            return

        current=self.head    
        while current.next is not None:
            if current.data <= target and current.next.data > target:
                break
            current = current.next
        if current.next is not None:
            current.next.prev=newnode
        newnode.next=current.next
        current.next=newnode
        newnode.prev=current
                
               

            
dll=dllist()
dll.append(2)
dll.append(4)
dll.append(6)
dll.append(8)
dll.print()
print()
dll.inserSorted(1)
dll.print()
