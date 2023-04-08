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

    def addNodeAfterValue(self, given_val, new_val):
        new_node=node(new_val)
        current=self.head
        if self.head.data==given_val:
            new_node.next=current.next
            self.head.next=new_node
            sll.print()
            return

        found=False
        while current is not None:
            if current.data==given_val:
                new_node.next=current.next
                current.next=new_node
                found=True
                break
            current=current.next    
        self.size+=1
        if found==True:
            sll.print()
        else:
            print('Data not found.')
            
 
sll=singlylinkedlist()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.print()
print()
sll.addNodeAfterValue(0,73)

