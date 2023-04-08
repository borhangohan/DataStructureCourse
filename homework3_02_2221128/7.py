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

    def reverse(self):
        def traverse_reverse(current):
            if current is not None:
                yield from traverse_reverse(current.next)
                yield current.data

        for data in traverse_reverse(self.head):
            sll_A.append(data) 

    
sll=singlylinkedlist()
sll_A=singlylinkedlist()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.print()
print()
sll.reverse()
sll_A.print()
