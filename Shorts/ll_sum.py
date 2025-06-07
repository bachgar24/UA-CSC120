## DON'T EDIT ANY CODE OTHER THAN THAT OF THE sum() METHOD YOU WRITE.
class LinkedList:
    def __init__(self):
        self._head = None
    
    # sum the nodes in the list
    def sum(self):
        # your code here  <<<
        output, next = 0, self._head
        while next != None:
            output += next.value()
            next = next.next()
        return output
    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    
    def __str__(self):
        string = 'LList -> '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        if self._next == None:
            reference = "-> None"
        else:
            reference = "-> "
        return str(self._value) + reference
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next