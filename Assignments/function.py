"""
    File: function.py
    Author: Garrett Bachman
    Course: CSC 144, Spring 2025
    Purpose: From a string input, converts them into sets and tests whether
    those sets form a valid function. Assumes that every element is one char,
    and that the ordered pairs input is an even length.
"""

def fix_domains(domain):
    """
    converts string domains into a set of values, numerics are converted to
    integers

    Parameters:
        domain (str): string of a domain or codomain

    Returns:
        set{}: set where each element is a char of domain
    """
    output = set()
    for char in domain:
        if char.isnumeric():
            output.add(int(char))
            
        else:
            output.add(char)
            
    return output

def fix_pairs(pairs):
    """
    converts string ordered pairs into a set containing them, converting 
    numeric values to ints

    Parameters:
        pairs (str): string of the ordered pairs

    Returns:
        set{tup()}: set of tuples representing the ordered pairs from pairs
    """
    output = set()
    pair = []
    for i in range(len(pairs)):
        if pairs[i].isnumeric():
            pair.append(int(pairs[i]))
            
        else:
            pair.append(pairs[i])
            
        if len(pair) == 2:
            output.add(tuple(pair))
            pair = []
    
    return output
            
def is_function(domain, codomain, pairs):
    """
    tests whether a domain, codomain, and set of ordered pairs forms a
    function

    Parameters:
        domain (set{}): set of values in the domain
        codomain (set{}): set of values in the codomain
        pairs (set{tup()}): set of tuples representing the ordered pairs

    Returns:
        tup(str): string message if the arguments form a function, and a
        message of why not if they don't
    """
    seen = set()
    for k, v in pairs:
        # test for illegal pairs
        if k not in domain or v not in codomain:
            return " not", "Members of the function do not exist in the "\
                + "domain or codomain"
        seen.add(k)
    
    # test for all members of domain present
    if len(seen) < len(domain):
        return " not", "Not all members of the domain appear on the left "\
            + "side of an ordered pair."
    
    
    # test for multiple images per preimage
    if len(seen) < len(pairs):
        return " not", "At least one member of the domain appears "\
                + "twice on the left side of an ordered pair."
    
    return "", ""

def main():
    domain = fix_domains(input("Enter the domain: "))
    codomain = fix_domains(input("Enter the codomain: "))
    pairs = fix_pairs(input("Enter the set of ordered pairs: "))
    is_func, error = is_function(domain, codomain, pairs)
    print("The set {} from {} to {} is{} a function."
          .format(pairs, domain, codomain, is_func))
    if error != "":
        print(error)
main()