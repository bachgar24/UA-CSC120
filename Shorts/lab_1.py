"""
    File: lab_1
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: contains three lab problems reviewing various otopics
"""

def dups_input():
    print("\n".join([input()]*2))
    
def is_short():
    inp = input()
    if len(inp) < 10:
        print("that's short!")
    elif len(inp) == 10:
        print("It's 10")
    else:
        print("That's long!")
        
def counting():
    small, big = int(input()), int(input())
    i = small
    while i <= big:
        print(i)
        i += 1

def main():
    dups_input()
    is_short()
    counting()

main()