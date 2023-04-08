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
    
    def delete_kth_element(self, k):
        if self.head is None:
            return None
        if k == 1:
            new_head = self.head.next
            self.head = new_head
            return new_head

        prev = None
        current = self.head
        i = 1
        while i < k and current is not None:
            prev = current
            current = current.next
            i += 1

        if current is not None:
            prev.next = current.next
            current.next = None

        return self.head

    def print_all(self, node):
        if node is None:
            return
        print(node.data)
        self.print_all(node.next)

ll=LinkedList()
ll.add_node(5)
ll.add_node(4)
ll.add_node(3)
ll.add_node(2)
ll.print_all(ll.head)
print()
ll.delete_kth_element(1)
ll.print_all(ll.head)