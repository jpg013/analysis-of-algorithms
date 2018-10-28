"""Double linked list implementation"""

class Node:
    """Node class contains a val attribute and pointer to next node in list"""
    
    def __init__(self, data):
        self.data = data
        self.prev = None # Initially prev points to nothing
        self.next = None # Initially next points to nothing

class DoublyLinkedList:
    """Doubly Linked List"""

    def __init__(self):
        self.head = None # initially the head points to None
        self.tail = None # initially the tail points to None

    def add(self, data):
        """Add node to head of list"""
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def remove(self):
        """Remove head of the list"""
        if self.head is None:
            raise Exception('cannot call remove on empty list')

        tmp = self.head
        
        # Set pointer of next node to None
        self.head = tmp.next
        self.head.prev = None
        
        return tmp

    def forward_traversal(self):
        """Forward Traversal through the doubly list, print each node data"""
        
        if self.head is None:
            raise Exception('cannot traverse an empty list')
        
        tmp = self.head

        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def backward_traversal(self):
        """Backward traversal through the doubly list, print each node data"""
        
        if self.head is None:
            raise Exception('cannot traverse an empty list')
        
        tmp = self.tail

        while(tmp):
            print(tmp.data)
            tmp = tmp.prev
    