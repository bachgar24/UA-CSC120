class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        
    def remove_last(self):
        if self._head == None:
            return
        
        current = self._head
        if current == self._tail:
            self._head = None
            self._tail = None
            return
        
        while current._next != self._tail:
            current = current._next
        current._next = None
        temp = self._tail
        self._tail = current
        return temp

    def add(self,new):
        new._next = self._head
        # if the list is empty, both
        # the head and tail will reference
        # this new node
        if self._head == None:
            self._tail = new 
        self._head = new 


    def __str__(self):
        string = 'LList -> '
        current = self._head
        while current != None:
            string += str(current)
            current = current._next
        return string + '; tail -> ' + str(self._tail)
  
class Node:
    def __init__(self,value):
        self._value = value
        self._next = None

    def __str__(self):
        if self._next == None:
            nxt = "None"
        else:
            nxt = "->"
        return " |" + str(self._value) + "|:" + nxt
        
def test01():
    ll = LinkedList()
    ll.add(Node(2))
    ll.add(Node(4))
    ll.add(Node(6))
    n = ll.remove_last()
    return str(ll)

def test02():
    ll = LinkedList()
    ll.add(Node(2))
    ll.add(Node(4))
    ll.add(Node(6))
    n = ll.remove_last()
    n = ll.remove_last()
    return str(ll)
    
def test03():
    ll = LinkedList()
    ll.add(Node(2))
    ll.add(Node(4))
    ll.add(Node(6))
    n = ll.remove_last()
    n = ll.remove_last()
    n = ll.remove_last()
    return str(ll)
    
def test04():
    ll = LinkedList()
    return ll.remove_last()