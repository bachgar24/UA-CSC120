class BinarySearchTree:
    def __init__(self):
        self._left = None
        self._right = None
        self._value = None
        
    def add(self, value):
        if self._value == None:
            self._value = value
            return
        
        
        if value < self._value:
            if self._left == None:
                t_bst = BinarySearchTree()
                t_bst.add(value)
                self._left = t_bst
                return
            
            self._left.add(value)
        
        else:
            if self._right == None:
                t_bst = BinarySearchTree()
                t_bst.add(value)
                self._right = t_bst
                return
            self._right.add(value)
            
    def find(self, value):
        if (self._value != value and self._left == None 
            and self._right == None):
            return
        
        if self._value == value:
            return self
        
        if value < self._value:
            return self._left.find(value)
        
        if value > self._value:
            return self._right.find(value)
    
    def __str__(self):
        return "({:d} {} {})".format( self._value, str(self._left), 
                                     str(self._right))