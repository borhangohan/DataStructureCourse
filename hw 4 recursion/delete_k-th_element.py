class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def delete_kth_node(self, node, k):
        if k == 1:
            self.head = node.next
            node=self.head
            return
        if node is None:
            return
        else:
            return self.delete_kth_node(node.next, k-1)
            
    def print_all(self, node):
        if node is None:
            return
        print(node.value)
        self.print_all(node.next)

ll=LinkedList()

ll.add_node(5)
ll.add_node(4)
ll.add_node(3)
ll.add_node(2)
ll.print_all(ll.head)

print()
# Delete the third node in the linked list (index 2)
ll.delete_kth_node(ll.head, 2)

ll.print_all(ll.head)