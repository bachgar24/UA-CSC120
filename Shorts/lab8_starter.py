#Lab 8 starter code
#Prob 4
class BinaryTree:
    def __init__(self,value):
        self._value = value
        self._left = None
        self._right = None

    def value(self):
        return self._value
    
    def left(self):
        return self._left
    
    def right(self):
        return self._right

    def set_left(self, bt):
        self._left = bt

    def set_right(self, bt):
        self._right = bt

    def __str__(self):
        if self == None:
            return 'None'
        else:
            return "({:d} {} {})".format(self._value
                , str(self._left), str(self._right))

def insert(tree, value):
    if tree == None:
        return BinaryTree(value)
    #assumes no duplicates
    if value < tree.value():
        bt = insert(tree.left(), value)
        tree.set_left(bt)
    elif value > tree.value():
        bt = insert(tree.right(), value)
        tree.set_right(bt)
    return tree

def first_matches_last(slist):
    if slist == []:
        return []
    if slist[0][-1] == slist[0][0]:
        return [slist[0]] + first_matches_last(slist[1:])
    return first_matches_last(slist[1:])

def display(slist):
    print("-"*len(slist[0]) + "\n" + dis_helper(slist) + "-"*len(slist[0]))
    
def dis_helper(slist):
    if slist == []:
        return ""
    return slist[0] + "\n" + dis_helper(slist[1:])

def expand(my_str, size):
    reps = size//len(my_str)
    excess = size%(reps * len(my_str))
    return my_str * reps + my_str[:excess]

def main():
    print(first_matches_last(["abba", "nope", "kook", "hello", "bob"]))
    print(display(["   *   ", "  ***  ", " ***** ", "*******"]))
    print(expand("ab", 7))
    print(expand("cat", 7))
    print(expand("boat", 7))
    
    # Below is the call to create the root node
    # of the binary search tree from problem 4:
    t = insert(None, 8)
    print(t)

    # Step 3: make the calls to insert for the
    #         remaining values: 10, 5, 20, 4, and 9
    #         print the tree after each call to insert
    
    insert(t, 10)
    print(t)
    insert(t, 5)
    print(t)
    insert(t, 20)
    print(t)
    insert(t, 4)
    print(t)
    insert(t, 9)
    print(t)
main()
