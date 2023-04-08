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

    def equalNode(self, other_list):
        if self.size != other_list.size:
            return False
        current1 = self.head
        current2 = other_list.head
        while current1 is not None and current2 is not None:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        return True


list_A=singlylinkedlist()
list_B=singlylinkedlist()
list_C=singlylinkedlist()
list_D=singlylinkedlist()

list_A.append(7)
list_A.append(6)
list_A.append(10)
list_A.append(11)

list_B.append(7)
list_B.append(6)
list_B.append(10)
list_B.append(11)

list_C.append(7)
list_C.append(16)
list_C.append(10)
list_C.append(11)

if list_A.equalNode(list_B):
    print("The lists are equal")
else:
    print("The lists are not equal")







