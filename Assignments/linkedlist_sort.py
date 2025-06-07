"""
    File: linkedlist_sort.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From an input file, creates a LinkedList of int Nodes, then
    prints a sorted version. Assumes one line of ints seperated by spaces.
"""
# class LinkedList
# An object of this class represents is a Linked List.
class LinkedList:
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        """
        sorts the nodes in the list, returning a new list
        
        Parameters:
            None
            
        Returns:
            LinkedList: new list with sorted nodes
        """
        sorted = LinkedList()
        while self._head != None:
            popped = self.remove()
            # adds to start if LL is empty or node is larger than the head
            if sorted._head == None or popped.value() >= sorted._head.value():
                sorted.add(popped)
            
            else:
                sort_node = sorted._head.next()
                prev = sorted._head
                
                # adds to end of LL if there is only one Node
                if sort_node == None:
                    sorted.insert(prev, popped)
                    
                while sort_node != None: 
                    # adds to Node previous to any lesser value Node
                    if popped.value() >= sort_node.value():
                        sorted.insert(prev, popped)
                        break
                    # adds Node to end of LL if there are no matches
                    if sort_node.next() == None:
                        sorted.insert(sort_node, popped)
                        break
                    
                    sort_node = sort_node.next()
                    prev = prev.next()
                    
        return sorted
            
    
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
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
        
                    
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next
    
def main():
    file = open(input())
    my_ll = LinkedList()
    for line in file:
        for num in line.split():
            my_ll.add(Node(int(num)))
            
    print(my_ll.sort())
    file.close()

main()