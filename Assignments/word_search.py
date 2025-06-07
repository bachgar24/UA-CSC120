"""
    File: word_search.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: uses inputted file names of a grid of letters and a list of words
    to find occurances of horizontal, vertical, and diagonal words in the grid
"""

def read_files():
    """
    creates word list and letter grid from file data

    Parameters:
        None

    Returns:  
        list[str], list[[str]]: word list and grid of lettters
    """ 
    word_file, letter_file = open(input(), "r"), open(input(), "r")
    word_list, letter_grid = [], []

    for line in word_file:
        word_list.append(line.strip())
    
    for line in letter_file:
        letter_grid.append(line.split())

    word_file.close()
    letter_file.close()
    return word_list, letter_grid

def words_in_row(word_list, row, reverse=True):
    """
    finds all words in a row of letters using the wordlist

    Parameters:
        word_list (list[str]): list of words to search for
        row (str): string of letters to find words in 
        reverse (bool, optional): whether to search the reverse of row. 
        Defaults to True.

    Returns:
        list[str]: list of all words found in the row
    """
    output = []
    for word in word_list:
        # find word in forward and reverse (optional)
        if (word.lower() in row
            or (word.lower() in row[::-1] and reverse)):
            output.append(word.lower())

    return output

def diagonal_construction(letter_grid, start_row, start_col):
    """
    loops from top left to bottom right to create a row of letters from
    starting indexes

    Parameters:
        letter_grid (list[[str]]): grid of letters
        start_row (int): starting row index
        start_col (int): starting col index

    Returns:
        str: row of diagonal letters as a string
    """
    output, row = "", start_row

    # from start row and col, change index down 1 right 1 per iteration
    for k in range(start_col, len(letter_grid)):
        output += letter_grid[row][k].lower()
        row += 1 
        if row >= len(letter_grid):
            break

    return output

def search_grid(word_list, letter_grid):
    """
    searches for words in the grid horizontally, vertically, and diagonally

    Parameters:
        word_list (list[str]): list of words to search for
        letter_grid (list[[str]]): grid of letters to search in

    Returns:
        list[str]: all words found in the grid from each search method
    """
    output = []

    # horizontal search
    for row in letter_grid:
        output.extend(words_in_row(word_list, "".join(row).lower()))
        
    # vertical search
    for i in range(len(letter_grid)):
        col = ""
        for row in letter_grid:
            col += row[i].lower()
        output.extend(words_in_row(word_list, col))
    
    # diagonal search
    # diagonals starting in col 0
    for i in range(len(letter_grid)-2):
        output.extend(words_in_row(word_list, 
                             diagonal_construction(letter_grid, i, 0), False))

    # diagonals starting in row 0
    for i in range(1, len(letter_grid)-2):
        output.extend(words_in_row(word_list, 
                             diagonal_construction(letter_grid, 0, i), False))

    return output

def print_words(searched_words):
    """
    prints each word in alphabetical order, one per line

    Args:
        searched_words (list[str]): list of words found in the grid
    """
    for word in sorted(searched_words):
        print(word)

def main():
    print_words(search_grid(*read_files()))
    
main()  