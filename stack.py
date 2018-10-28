from singly_linked_list import SinglyLinkedList

class Stack:
    """Stack data structure implementation using linked list"""
    
    def __init__(self, max_size):
        if not isinstance(max_size, int):
            raise Exception('size must be int greater than 0')
        
        if (max_size < 1):
            raise Exception('size must be int greater than 0')

        self.top = 0
        self.max_size = max_size
        self.llist = SinglyLinkedList()

    
    def push(self, val):
        """Push item onto stack"""
        
        if self.top >= self.max_size:
            raise Exception('Stack is full')

        self.llist.add(val)
        self.top += 1

    def pop(self):
        """Pop item from stack"""
        
        if self.top == 0:
            raise Exception('Stack is empty')
        
        self.top -= 1
        return self.llist.remove()