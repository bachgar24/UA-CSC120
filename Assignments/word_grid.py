"""
    File: word_grid.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: uses the python random library as well as 2d lists to create 
    grids with seeded values, printing the contents of each row
"""

from random import *

def init():
    """
    initializes grid size and seed from input

    Parameters:
        None

    Returns:  
        int: size of the grid
    """ 
    grid_size = int(input())
    seed_value = input()
    seed(seed_value)

    return grid_size

def make_grid(grid_size):
    """
    creates a square grid from inputted dimensions populated by random letters

    Parameters:
        grid_size (int): size of grid to create

    Returns:  
        list[[str]]: created grid
    """ 
    output = []
    for i in range((grid_size)):
        output.append([])
        for k in range((grid_size)):
            # converts random int value to ascii chars
            output[i].append(chr(randint(97, 122)))

    return output

def print_grid(grid):
    """
    prints a 2d grid with values split by commas and each row on a new line

    Parameters:
        grid list[[str]]: 2d grid of letters to print

    Returns:  
        None
    """ 
    for row in grid:
        print(",".join(row))



def main():
    print_grid(make_grid(init()))

main()