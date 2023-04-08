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

    def numOfOccurrences(self, val):
        count=0
        current=self.head
        while current is not None:
            if val==current.data:
                count+=1
            current=current.next
        return count   

sll=singlylinkedlist()
sll.append(1)
sll.append(7)
sll.append(7)
sll.append(7)
sll.append(9)
sll.print()    
print('\nTotal Occurrences:',sll.numOfOccurrences(7))