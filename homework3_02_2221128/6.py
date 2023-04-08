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

    def sorted_insert(self, target):
        newnode=node(target)
        if self.head.data>target:
            newnode.next=self.head
            self.head=newnode
            return

        current=self.head    
        while current.next is not None and current.next.data < target:
            current = current.next
        newnode.next=current.next
        current.next=newnode

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

sll.sorted_insert(5.5)
sll.print()

