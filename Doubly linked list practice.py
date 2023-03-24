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
            print(current.data, end=' <=> ')
            current=current.next
    
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True  
            current = current.next
        return False

    def summation(self):
        current=self.head
        sum=0
        while current!=None:
            sum+=current.data
            current=current.next
        print(sum)

    def add_from_a_specific_int(self,specific_data):
        current=self.head
        data_found=False
        sum=0
        if self.search(specific_data) is True:
            while current!=None:
                if data_found:
                    sum+=current.data
                if current.data==specific_data:
                    data_found=True
                current=current.next
            print(sum)
        else:
            print('not found')
    def add_before_data(self, specific_data):
        current=self.tail
        data_found=False
        sum=0
        if self.search(specific_data):
            while current is not None:
                if data_found:
                    sum+=current.data
                if current.data==specific_data:
                    data_found=True
                current=current.prev
            print(sum)
        else:
            print('not found')

    def traverse(self):
        current=self.head
        while current is not None:
            yield current.data
            current=current.next
            
#TWO WAYS OF FINDING SUM BEFORE TARGETED DATA
    def sum_before(self, target_data):
        sum=0
        for data in self.traverse():
            if data==target_data:
                break
            if self.head is not None:
                sum+=data
        return sum
        
    def sum_before_data(self, target_data):
        sum=0
        current=self.head
        while current is not None:
            if target_data==current.data:
                break
            sum+=current.data
            current=current.next
        return sum

dll=dllist()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.print()
print()
#print(dll.size)
#print(dll.search(1))
#dll.summation()
#dll.add_from_a_specific_int(2)
#dll.add_before_data(3)
print(dll.sum_before(2))
