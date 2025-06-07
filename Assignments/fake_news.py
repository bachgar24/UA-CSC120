"""
    File: fake_news.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From a csv file, creates a descending-sorted LinkedList of 
    cleaned words as string Nodes, then prints the words with occurrences
    greater than that of an inputted index. Assumes element of interest is in
    col. 4 of the csv file, and elements contain only ascii characters.
"""
from csv import *
from string import *

class Node:
    """
        This class represents a node to be used in a LinkedList.

        The class defines:
            an incr() method that increments the count of the Node,
            a ge() method that compares two Nodes by their counts,
            and a str() method.
        Requires a string word on construction.
    """
    def __init__(self, word):
        """
        constructor for Node objects; sets _word to word, creates _count set
        to 1, and creates _next to None
        
        Parameters:
            word (str): string to initailize Node with

        Returns:
            None
        """
        self._word = word
        self._count = 1
        self._next = None
        
    def word(self):
        return self._word
    
    def count(self):
        return self._count
    
    # from PA05-L
    def next(self):
        return self._next
    
    def set_next(self, target):
        self._next = target
        
    def incr(self):
        """
        increments the count by 1
        
        Parameters:
            None

        Returns:
            None
        """
        self._count += 1
    
    def __ge__(self, other):
        """
        compares two Nodes for use in sorting

        Parameters:
            other (Node): Node to compare against

        Returns:
            bool: if self's count is greater than or equal to other's count
        """
        return self._count >= other.count()
    
    # from PA05-L    
    def __str__(self):
        return str(self._word + " " + self._count) + "; "
    
class LinkedList:
    """
        This class represents a linkedlist as a collection of Nodes.

        The class defines:
            a sort() method that sorts the list in descending order,
            an is_empty() method that returns if the list is empty,
            an update_count() method that increments the count of existing 
            Nodes and adds non-existent Nodes,
            a get_nth_highest_count() method that finds the Node at a given
            index,
            a print_upto_count() method that prints all Nodes with counts no
            less than a given count,
            an add() method that adds Nodes to the head of the list,
            a rm_from_hd() method that pops Nodes from the head of the list,
            an insert_after() method that inserts one Node after another,
            and a str() method.
        Requires no arguments on construction.
    """
    # from PA05-L
    def __init__(self):
        self._head = None
    
    def sort(self):
        """
        sorts the nodes in the list, reassigning to self._head
        
        Parameters:
            None
            
        Returns:
            LinkedList: new list with sorted nodes
        """
        sorted = LinkedList()
        while self._head != None:
            popped = self.rm_from_hd()
            # adds to start if LL is empty or node is larger than the head
            if sorted._head == None or popped >= sorted._head:
                sorted.add(popped)
            
            else:
                sort_node = sorted._head.next()
                prev = sorted._head
                
                # adds to end of LL if there is only one Node
                if sort_node == None:
                    sorted.insert_after(prev, popped)
                    
                while sort_node != None: 
                    # adds to Node previous to any lesser value Node
                    if popped >= sort_node:
                        sorted.insert_after(prev, popped)
                        break
                    # adds Node to end of LL if there are no matches
                    if sort_node.next() == None:
                        sorted.insert_after(sort_node, popped)
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
    
    def head(self):
        return self._head
    
    def update_count(self, word):
        """
        if word is present in the list, increments its count; otherwise, adds
        a node for it with count initialized to 1

        Parameters:
            word (str): word to check for in the list

        Returns:
            None
        """
        current = self._head
        while current != None:
            if current.word() == word:
                current.incr()
                break
            current = current.next()
        else:
            self.add(Node(word))
            
    def get_nth_highest_count(self, n): 
        """
        returns the count associated with the node in the linked list at 
        position n

        Parameters:
            n (int): index of word to get count of

        Returns:
            int: count of word at index n
        """
        current = self._head
        counter = 0
        while current != None:
            if counter == n:
                return current.count()
            
            counter += 1
            current = current.next()
        
        return 0
    
    def print_upto_count(self, n):
        """
        prints out all the words that have count at least n

        Args:
            n (int): count to compare against

        Returns:
            None
        """
        current = self._head
        while current != None:
            if current.count() >= n:
                print("{} : {:d}".format(current.word(), current.count()))
            current = current.next()
            
    # add a node to the head of the list; from PA05-L
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node; from PA05-L
    def rm_from_hd(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1; from PA05-L
    def insert_after(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
        
    # from PA05-L
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
    
def process_title(title):
    """
    omits any words with length less than or equal to 2, splits on punctuation
    and whitespace, then returns remaining words as a list in lowercase

    Parameters:
        title (str): title to edit

    Returns:
        list[str]: cleaned list of words in title
    """
    for i in range(len(title)):
        if title[i] in punctuation:
            title = title[:i] + " " + title[i+1:]
            
    output = title.split()
    
    for i in range(len(output)-1, -1, -1):
        if len(output[i]) <= 2:
            output.pop(i)
            
        else:
            output[i] = output[i].lower()
    return output

def read_file(filename):
    """
    reads a csv file, storing occurrences of each word in column 4 in a 
    LinkedList and returning the sorted result

    Parameters:
        filename (str): path to file to iterate over

    Returns:
        LinkedList: words sorted by their occurrences, descending
    """
    file = open(filename)
    csvreader = reader(file)
    word_ll = LinkedList()
    for line in csvreader:
        title = process_title(line[4])
        for word in title:
            word_ll.update_count(word)
    
    word_ll.sort()
    file.close()
    return word_ll

def main():
    sorted_ll = read_file(input()) 
    sorted_ll.print_upto_count(sorted_ll.get_nth_highest_count(int(input())))
    
main()