"""
    File: friends.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From a .txt file, adds pairs of friends to a linkedlist, then
    compares the mutual friends of two inputted people and prints the result.
    Assumes pairs will be split by whitespace, while only the first and last 
    two names in a line will be considered, intended for a complete overlap.
"""
from linked_list import *

def add_pair(pair, master_ll):
    """
    loops through master_ll to add the first element of pair if not in the
    list, with the second element of pair always added to the friend list of
    the first

    Parameters:
        pair (list): friend pairing
        master_ll (LinkedList): list containing the first dimension of people
        
    Returns:
        None
    """
    node = master_ll.update_friend(pair[0].capitalize())
    node.friends().update_friend(pair[1].capitalize())
    
def read_file(filename, master_ll):
    """
    reads a file, adding all friend pairs into master_ll

    Parameters:
        filename (str): path to file to iterate over
        master_ll (LinkedList): list containing the first dimension of people

    Returns:
        LinkedList: mutated list with additions from the file
    """
    file = open(filename)
    for line in file:
        pair = line.split()
        add_pair(pair, master_ll)
        add_pair(pair[::-1], master_ll)
        
    file.close()
    return master_ll
    
def common_friends(name1, name2, master_ll):
    """
    from two names, finds the nodes in master_ll and searches for mutual
    friends. If any are found, prints the results in alphabetical order

    Parameters:
        name1 (str): name of first person to compare
        name2 (str): name of second person to compare
        master_ll (LinkedList): list containing the first dimension of people
        
    Returns:
        None
    """
    node1, node2 = master_ll.find_name(name1.capitalize()),\
                   master_ll.find_name(name2.capitalize())
                   
    # breaks function if either name is not present in master_ll
    if node1 == None:
        print("ERROR: Unknown person", name1.capitalize())
        return
    elif node2 == None:
        print("ERROR: Unknown person", name2.capitalize())
        return
    
    mutuals = LinkedList()
    current = node1.friends().head()
    while current != None:
        if node2.friends().find_name(current.name()) != None:
            mutuals.add(Node(current.name()))
        current = current.next()
    
    # skips printing if there are no mutual friends  
    if mutuals.is_empty():
        return
    
    mutuals.sort()
    current = mutuals.head()
    print("Friends in common: ")
    while current != None:
        print(current.name())
        current = current.next()
    
def main():
    master_ll = read_file(input("Input file: "), LinkedList())
    common_friends(input("Name 1: "), input("Name 2: "), master_ll)
    
main()