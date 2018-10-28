"""Singly linked list implementation"""

class Node:
    """Node class contains a val attribute and pointer to next node in list"""
    
    def __init__(self, val):
        self.val = val
        self.next = None # Initially the node points to nothing

class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self):
        self.head = None # initially the head points to None

    def add(self, node):
        """Add node to head of list"""
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def remove(self):
        """Remove head of the list"""
        if self.head is None:
            raise Exception('cannot call remove_head on empty list')

        tmp = self.head
        self.head = tmp.next
        
        return tmp

    def get_node_at_position(self):
        return None

    def remove_tail(self):
        """Find and return the tail node of the linked list"""
        tmp = self.head

        if tmp is None:
            return tmp

        # Check if head is tail
        if self.is_tail_node(tmp):
            self.head = None
            return tmp
        
        while(tmp):
            tail = tmp.next

            if self.is_tail_node(tmp.next):
                tmp.next = None
                return tail
            
            tmp = tmp.next

    def is_tail_node(self, node):
        """Helper method to determine whether a node is a tail"""
        return node.next is None