def preorder_to_bst(preorder):
    if preorder == []:
        return
    
    tree = BinarySearchTree(preorder[0])
    preorder = preorder[1:]
    left, right = [], []
    for value in preorder:
        if value < tree._value:
            left.append(value)
        
        else:
            right.append(value)
    
    tree._left = preorder_to_bst(left)
    tree._right = preorder_to_bst(right)
    return tree

"""DO NOT MODIFY ANYTHING BELOW THIS LINE"""
class BinarySearchTree:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def __str__(self):
        if self == None:
            return 'None'
        else:
            return "({:d} {} {})".format(self._value
                , str(self._left), str(self._right))

def test01():
    tree = preorder_to_bst([3])
    return str(tree)

def test02():
    tree = preorder_to_bst([3, 2, 5])
    return str(tree)

def test03():
    tree = preorder_to_bst([8, 5, 11, 9, 14])
    return str(tree)

def test04():
    tree = preorder_to_bst([24, 11, 5, 7, 30, 28, 41])
    return str(tree)