"""
    File: huffman.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From a file, builds a binary tree and decodes the tree from the
    file's provided Huffman encoding sequence. Assumes the file contains the
    preorder and postorder traversals on seperate, consecutive lines in that
    order, where each element is a unique integer seperated by whitespace.
    Assumes the Huffman sequence is on the third line and consists of only
    ones and zeroes.
"""

class BinaryTree:
    """
        This class represents a binary tree.

        The class defines:
            an is_leaf() method that checks if the node is a leaf,
            a postorder() method that creates a postorder traversal of the 
            BinaryTree,
            and a str() method drived from PA-9S.
        Requires a value argument of any type on construction.
    """
    def __init__(self, value):
        """
        constructor for BinaryTree objects; sets self._value to value, creates
        self._left to None, creates self._right to None. Derived from PA-8S

        Parameters:
            value (any): value to assign to the head node of the BinaryTree
            
        Returns:
            None
        """
        self._value = value
        self._left = None
        self._right = None

    def value(self):
        return self._value

    def left(self):
        return self._left

    def right(self):
        return self._right
    
    def set_left(self, tree):
        self._left = tree
        
    def set_right(self, tree):
        self._right = tree
            
    def is_leaf(self):
        """
        shortcut method to check if the head node of the BinaryTree is a leaf

        Parameters:
            None
            
        Returns:
            bool: if the node is a leaf
        """
        return self._left == None and self._right == None
    
    def postorder(self):
        """
        recursive method that creates the postorder traversal of the
        BinaryTree

        Parameters:
            None

        Returns:
            str: postorder traversal of the BinaryTree
        """
        output = ""
        if self._left != None:
            output += self._left.postorder()
        
        if self._right != None:
            output += self._right.postorder()
        
        return output + str(self._value)
    
    def __str__(self):
        return "({:d} {} {})".format( self._value, str(self._left), 
                                     str(self._right))
            
def read_file(filename):
    """
    reads the input file and returns a list where each line is an element

    Parameters:
        filename (str): path to file to read

    Returns:
        list[str]: list of every line in the file
    """
    file = open(filename)
    contents = file.read().strip().split("\n")
    file.close()
    return contents
    
def build_tree(preorder, inorder):
    """
    recursive function to create a BinaryTree from its preorder and inorder
    traversals

    Parameters:
        preorder (list[int]): preorder traversal of the tree
        inorder (list[int]): inorder traversal of the tree

    Returns:
        BinaryTree: completed BinaryTree
    """
    if preorder == []:
        return None
    
    # add first element of preorder
    tree = BinaryTree(int(preorder[0]))
    preorder = preorder[1:]
        
    # split order lists into subtrees and add to current tree
    idx = inorder.index(str(tree.value()))
    left = inorder[:idx]
    tree.set_left(build_tree(preorder[:len(left)], left))
    tree.set_right(build_tree(preorder[len(left):], inorder[idx + 1:]))
    
    # return tree with filled subtrees
    return tree

def decode_tree(encoding, subtree, tree):
    """
    recursive function that uses a huffman encoding sequence to decode a
    BinaryTree

    Parameters:
        encoding (list[str]): encoding sequence
        subtree (BinaryTree): current iteration's BinaryTree
        tree (BinaryTree): original tree to return to after completing a path

    Returns:
        str: all leaf node values reached by encoding
    """
    if encoding == "" and (not subtree.is_leaf() or subtree == tree):
        return ""
    
    # return case; tree is leaf node
    if subtree.is_leaf():
        return str(subtree.value()) + decode_tree(encoding, tree, tree)
    
    # go right on 1
    if int(encoding[0]):
        next_subtree = subtree.right()
    
    # go left on 0
    else:
        next_subtree = subtree.left()
        
    # return to top if encoding path fails
    if next_subtree == None:
        return decode_tree(encoding[1:], tree, tree)
    
    return decode_tree(encoding[1:], next_subtree, tree)
    

def main():
    contents = read_file(input('Input file: '))
    preorder, inorder, encoding =\
        contents[0].split(), contents[1].split(), contents[2]
    tree = build_tree(preorder, inorder)
    print(tree.postorder())
    print(decode_tree(encoding, tree, tree))
    
main()