class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            
    def print_all(self, node):
        if node is None:
            return
        else:
            print(node.data)
            return self.print_all(node.next)
        
    def printall(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

sll=LinkedList()

sll.add_node(5)
sll.add_node(4)
sll.add_node(3)
sll.add_node(2)
sll.print_all(sll.head)