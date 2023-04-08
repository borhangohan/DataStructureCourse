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
    
    def reverse(self, node):
        if node is None:
            return
        # swap prev and next attributes of the current node
        temp = node.prev
        node.prev = node.next
        node.next = temp
        # recursively call reverse on the next node
        if node.prev is None:
            self.head = node
        else:
            return self.reverse(node.prev)
              
dll=dllist()
dll.append(2)
dll.append(4)
dll.append(6)
dll.append(8)
dll.print()
print()
dll.reverse(dll.head)
dll.print()
