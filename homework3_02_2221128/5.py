class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class singlylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
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

    def remove_even(self):
        while self.head is not None and self.head.data%2==0:
            self.head=self.head.next
            self.size-=1

        current=self.head
        while current.next is not None:
            if current.next.data%2==0:
                current.next=current.next.next
                self.size-=1
            else:
                current=current.next
'''
#Using generator=>
    def traverse(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next  

    def delete_even(self):
        current=self.head
        prev=None
        for data in self.traverse():
            if data%2==0:
                if prev is None:
                    self.head=current.next
                else:
                    prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
'''        
    
sll=singlylinkedlist()
sll.append(2)
sll.append(4)
sll.append(5)
sll.append(6)

sll.append(7)
sll.append(8)
sll.append(9)
sll.append(10)
sll.append(11)
sll.print()
print()

sll.remove_even()
sll.print()

