
"""
    File: writer_bot_ht.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: Uses a Markov chain algorithm to generate new text from a file,
    using a hashtable ADT to store prefixes and suffixes. Assumes the file 
    contains elements split by whitespace, and uses the random seed 8 to 
    generate the text.
"""
from random import *
from sys import *

SEED = 8
NONWORD = "@"

class Hashtable:
    """
        This class represents a hash table that uses linear probing to handle
        collisions.

        The class defines:
            a _hash() private method that 
            a put() method that 
            a get() method that 
            a contains() method, and a str() method.
        Requires a integer size argument on construction.
    """

    def __init__(self, size):
        """
        constructor for Hashtable objects; creates _pairs to a list of length
        size, sets _size to size

        Parameters:
            size (int): size of the hashtable
        
        Returns:
            None
        """
        self._pairs = [None]*size
        self._size = size
        
    def _hash(self, key):
        """
        hashing method using Horner's rule to compute the polynomial

        Parameters:
            key (str): key to convert

        Returns:
            int: hashed value of key
        """
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size
    
    def put(self, key, value):
        """
        hashes key and inserts the key/value pair in the Hashtable, using
        linear probing with a decrement of 1 to resolve collisions

        Parameters:
            key (str): key to insert
            value (str): value to insert
        
        Returns:
            None
        """
        hash = self._hash(key)
        while self._pairs[hash] != None:
            hash -= 1
        self._pairs[hash] = [key, [value]]
        
    def get(self, key):
        """
        looks up key in the hash table and returns the corresponding value

        Parameters:
            key (str): key to search for in the Hashtable

        Returns:
            list[str]: list of all values, or None if not found
        """
        hash = self._hash(key)
        while self._pairs[hash] != None:
            if self._pairs[hash][0] == key:
                return self._pairs[hash][1]
            hash -= 1
            
    def __contains__(self, key):
        return self.get(key) != None
    
    def __str__(self):
        output = ""
        for i in range(self._size):
            if self._pairs[i] == None:
                continue
            output += "hash table at index " + str(i) + " is "\
                       + str(self._pairs[i]) + "\n"
        return output

def read_file(filename):
    """
    reads a file and adds every word split on whitespace to a list. Adapted 
    from PA-9L

    Parameters:
        filename (str): path to file to read

    Returns:
        list[str]: every word from the file in a list, in original order
    """
    file = open(filename)
    output = file.read().split()
    file.close()
    return output

def markov_build(text, table_size, prefix_size):
    """
    creates a Markov chain table using a Hashtable, priming the first n
    entries, where n=prefix_size, with the constant NONWORD. Adapted from
    PA-9L

    Parameters:
        text (list[str]): list of words from a text
        prefix_size (int): how many words to use for each prefix

    Returns:
        HashTable: table mapping string prefixes to lists of suffixes
    """
    table = Hashtable(table_size)
    
    # prime table with NONWORD
    for i in range(prefix_size):
        table.put(((NONWORD + " ")*(prefix_size-i)
                   + " ".join(text[:i])).rstrip(), text[i])
        
    for i in range(len(text)-prefix_size):
        # create prefix containing the next prefix_size words, with overlap
        prefix = " ".join(text[i:i+prefix_size])
        suffix = text[i+prefix_size]
        
        # if prefix does not exist, add it with the suffix
        if not prefix in table:
            table.put(prefix, suffix)
        
        # if existing, add suffix to the list of values of the prefix
        else:
            table.get(prefix).append(suffix)
        
    return table

def markov_generate(table, words, prefix_size):
    """
    creates a Markov chain text of a length words using a Markov chain table
    represented by a Hashtable. Adapted from PA-9L

    Parameters:
        HashTable: Markov chain table mapping string prefixes to lists of 
        suffixes
        words (int): length of text to generate
        prefix_size (int): words per prefix, used for primed table

    Returns:
        list[str]: list of words of generated text
    """
    output = []
    
    # use NONWORD primer to start generation
    prefix = ((NONWORD + " ") * prefix_size).rstrip()
    
    while prefix in table and len(output) < words:
        val = table.get(prefix)
        
        if len(val) == 1:
            suffix = val[0]
        
        # if there are more than one suffix, randomly choose one and append
        else:
            suffix = val[randint(0, len(val)-1)]
            
        output.append(suffix)
        
        # shift the prefix right 1 and add the suffix
        prefix = (prefix.partition(" ")[2] + " " + suffix).strip()
    
    return output

def print_text(text):
    """
    prints a list with max 10 elements per line. Adapted from PA-9L

    Parameters:
        text (list[]): list of elements to print
        
    Returns:
        None
    """
    for i in range(0, len(text), 10):
        print(" ".join(text[i:i+10]).rstrip())
        

def main():
    seed(SEED)
    
    filename, table_size, prefix_size, words =\
        input(), int(input()), int(input()), int(input())
        
    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        exit(0)
        
    if words < 1:
        print("ERROR: specified size of the generated text is less than one")
        exit(0)
        
    table = markov_build(read_file(filename), table_size, prefix_size)
    print_text(markov_generate(table, words, prefix_size))
main()