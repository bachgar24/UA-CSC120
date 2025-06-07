"""
    File: writer_bot.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: Uses a Markov chain algorithm to generate new text from a file.
    Assumes the file contains elements split by whitespace, and uses the
    random seed 8 to generate the text.
"""
from random import *

SEED = 8
NONWORD = " "

def read_file(filename):
    """
    reads a file and adds every word split on whitespace to a list

    Parameters:
        filename (str): path to file to read

    Returns:
        list[str]: every word from the file in a list, in original order
    """
    file = open(filename)
    output = file.read().split()
    file.close()
    return output

def markov_build(text, prefix_size):
    """
    creates a Markov chain table using a dictionary, priming the first n 
    entries, where n=prefix_size, with the constant NONWORD

    Parameters:
        text (list[str]): list of words from a text
        prefix_size (int): how many words to use for each prefix

    Returns:
        dict{(str):[str]}: dict mapping tuples of prefixes to the list of 
        their suffixes
    """
    table = dict()
    
    # prime table with NONWORD
    for i in range(prefix_size):
        table[tuple([NONWORD]*(prefix_size-i) + text[:i])] = [text[i]]
        
    for i in range(0, len(text)-prefix_size):
        # create prefix containing the next prefix_size words, with overlap
        prefix = tuple(text[i:i+prefix_size])
        
        # if prefix does not exist, add it with no suffixes
        if prefix not in table:
            table[prefix] = []
            
        # add suffix to the list of values of the prefix
        table[prefix].append(text[i+prefix_size])
        
    return table

def markov_generate(table, words):
    """
    creates a Markov chain text of a length words using a Markov chain table
    represented by a dictionary

    Parameters:
        table (dict{(str):[str]}): Markov chain dict mapping tuples of
        prefixes to the list of their suffixes
        words (int): length of text to generate

    Returns:
        list[str]: list of words of generated text
    """
    output = []
    # find length of prefixes
    for key in table:
        prefix_size = len(key)
        break
    
    # use NONWORD primer to start generation
    prefix = [NONWORD] * prefix_size
    # save the current prefix as a tuple for easy access
    key = tuple(prefix)
    
    while key in table and len(output) < words:
        val = table[key]
        
        if len(val) == 1:
            suffix = val[0]
        
        # if there are more than one suffix, randomly choose one
        else:
            suffix = val[randint(0, len(val)-1)]
            
        # append suffix to the generated text
        output.append(suffix)
        
        # shift the prefix right 1 and add the suffix
        prefix = prefix[1:] + [suffix]
        key = tuple(prefix)
    
    return output

def print_text(text):
    """
    prints a list with max 10 elements per line

    Parameters:
        text (list[]): list of elements to print
    """
    for i in range(0, len(text), 10):
        print(" ".join(text[i:i+10]).strip())
        

def main():
    seed(SEED)
    filename, prefix_size, words = input(), int(input()), int(input())
    table = markov_build(read_file(filename), prefix_size)
    print_text(markov_generate(table, words))
main()