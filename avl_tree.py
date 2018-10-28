class TreeNode(object):
    """Tree Node Class"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def get_height(self, root):
        if not root:
            return 0
        
        return root.height

    def get_balance(self, root): 
        if not root: 
            return 0
  
        return self.get_height(root.left) - self.get_height(root.right) 
    
    def insert(self, data, root=None):
        if not root:
            return TreeNode(data)
        
        if data < root.data:
            root.left = self.insert(data, root.left)
        else:
            root.right = self.insert(data, root.right)

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root) 

        if balance < -1 and data > root.right.data: 
            return self.rotate_left(root) 

        return root

    def rotate_left(self, z): 
        y = z.right 
        T2 = y.left 
  
        y.left = z 
        z.right = T2 
  
        z.height = 1 + max(
            self.get_height(z.left), 
            self.get_height(z.right)
        ) 

        y.height = 1 + max(
            self.get_height(y.left), 
            self.get_height(y.right)
        ) 
  
        # Return the new root 
        return y 

    def rotate_right(self, z): 
        y = z.left 
        T3 = y.right 

        y.right = z 
        z.left = T3 

        z.height = 1 + max(
            self.get_height(z.left), 
            self.get_height(z.right)
        ) 

        y.height = 1 + max(
            self.get_height(y.left), 
            self.get_height(y.right)
        ) 

        # Return the new root 
        return y 