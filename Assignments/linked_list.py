"""
    File: linked_list.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: Contains LinkedList-related classes and methods. To be used
    specifically for importing to friends.py.
"""

                   
class Node:
    """
        This class represents a node to be used in a LinkedList.

        The class defines:
            a le() method that compares two Nodes by their names,
            and a str() method.
        Requires a string name on construction.
    """
    def __init__(self, name):
        """
        constructor for Node objects; sets _name to name, creates _count set
        to 1, and creates _next to None
        
        Parameters:
            word (str): string to initailize Node with

        Returns:
            None
        """
        self._name = name
        self._friends = LinkedList()
        self._next = None
    
    def name(self):
        return self._name
    
    def friends(self):
        return self._friends
    
    def next(self):
        return self._next
    
    def set_next(self, node):
        self._next = node
        
    def __le__(self, other):
        """
        compares two Nodes for use in sorting

        Parameters:
            other (Node): Node to compare against

        Returns:
            bool: if self's name is less than or equal to other's name
        """
        return self._name <= other.name()
    
    def __str__(self):
        return str(self._name) + ": " + str(self._friends) + "; "
    
class LinkedList:
    """
        This class represents a linkedlist as a collection of Nodes.

        The class defines:
            a sort() method that sorts the list in descending order,
            an is_empty() method that returns if the list is empty,
            an update_friend() method that adds a new Node to the list if it
            doesn't exist, returning the relevant Node,
            a find_name() method that searches the list for a Node and returns
            it, 
            an add() method that adds Nodes to the head of the list,
            a remove() method that pops Nodes from the head of the list,
            an insert() method that inserts one Node after another,
            and a str() method.
        Requires no arguments on construction.
    """
    def __init__(self):
        """
        constructor for LinkedList objects; creates self._head to None
        
        Parameters:
            None
            
        Returns:
            None
        """
        self._head = None
        
    def sort(self):
        """
        sorts the nodes in the list in ascending order, reassigning to
        self._head. Adapted from PA05-L
        
        Parameters:
            None
            
        Returns:
            None
        """
        sorted = LinkedList()
        while self._head != None:
            popped = self.remove()
            # adds to start if LL is empty or node is lesser than the head
            if sorted.head() == None or popped <= sorted.head():
                sorted.add(popped)
                continue
        
            sort_node = sorted.head().next()
            prev = sorted.head()
            
            # adds to end of LL if there is only one Node
            if sort_node == None:
                sorted.insert(prev, popped)
                
            while sort_node != None: 
                # adds to Node previous to any greater value Node
                if popped <= sort_node:
                    sorted.insert(prev, popped)
                    break
                
                # adds Node to end of LL if there are no matches
                if sort_node.next() == None:
                    sorted.insert(sort_node, popped)
                    break
                
                sort_node = sort_node.next()
                prev = prev.next()
                    
        self._head = sorted.head()
        
    def is_empty(self):
        """
        indicates whether or not the list contains any nodes
        
        Parameters:
            None

        Returns:
            bool: if head points to None
        """
        return self._head == None
       
    def update_friend(self, name):
        """
        if name is present in the list, returns Node of the name. Otherwise,
        adds and returns new Node with the name

        Parameters:
            name (str): name of person to check or add

        Returns:
            Node: changed or added Node
        """
        existing_node = self.find_name(name)
        if existing_node != None:
            return existing_node
        
        new_node = Node(name)
        self.add(new_node)
        return new_node
    
    def find_name(self, name):
        """
        searches self for a Node with name, returns if found

        Parameters:
            name (str):  name of person to search for

        Returns:
            Node: found Node
            None: if Node not found
        """
        current = self._head
        while current != None:
            if current.name() == name:
                return current
            current = current.next()
    
    def add(self, node):
        """
        adds a Node to the head of the list. From PA05-L

        Parameters:
            node (Node): Node to add
            
        Returns: 
            None
        """
        node.set_next(self._head)
        self._head = node
      
    def remove(self):
        """
        remove a Node from the head of the list and returns the Node. From
        PA05-L

        Parameters:
            None
            
        Returns:
            Node: popped Node
        """
        assert self._head != None
        _node = self._head
        self._head = _node.next()
        _node.set_next(None)
        return _node
    
    def insert(self, node1, node2):
        """
        inserts node2 after node1 in the list. From PA05-L

        Parameters:
            node1 (Node): Node coming before node2
            node2 (Node): Node to be inserted after node1

        Returns:
            None
        """
        assert node1 != None
        node2.set_next(node1.next())
        node1.set_next(node2)
    
    def head(self):
        return self._head
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string