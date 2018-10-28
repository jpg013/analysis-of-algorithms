"""Singly linked list implementation"""

class Node:
    """Node class contains a val attribute and pointer to next node in list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None # Initially the node points to nothing

class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self):
        self.head = None # initially the head points to None

    def add(self, data):
        """Add node to head of list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def remove(self):
        """Remove head of the list"""
        if self.head is None:
            raise Exception('cannot call remove on empty list')

        tmp = self.head
        self.head = tmp.next
        
        return tmp.data

    def remove_tail(self):
        """Find and return the tail node of the linked list"""
        if self.head is None:
            raise Exception('cannot call remove_tail on empty list')
        
        tmp = self.head

        # Check if head is tail
        if self.is_tail_node(tmp):
            self.head = None
            return tmp
        
        while(tmp):
            tail = tmp.next

            if self.is_tail_node(tmp.next):
                tmp.next = None # Remove reference to tail
                return tail.data
            
            tmp = tmp.next

    def is_tail_node(self, node):
        """Helper method to determine whether a node is a tail"""
        return node.next is None