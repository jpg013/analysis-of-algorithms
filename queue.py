from singly_linked_list import SinglyLinkedList

class Queue:
    """Queue data structure implementation using linked list"""
    
    def __init__(self, max_size):
        if not isinstance(max_size, int):
            raise Exception('size must be int greater than 0')
        
        if (max_size < 1):
            raise Exception('size must be int greater than 0')

        self.top = 0
        self.max_size = max_size
        self.llist = SinglyLinkedList()

    def enqueue(self, val):
        """add item into queue"""
        
        if self.top >= self.max_size:
            raise Exception('Queue is full')

        self.llist.add(val)
        self.top += 1

    def dequeue(self):
        """remove item from queue"""
        
        if self.top == 0:
            raise Exception('Queue is empty')
        
        self.top -= 1
        return self.llist.remove_tail()