def tree_sum(tree):
    if tree == None:
        return 0
    return tree_sum(tree.left()) + tree_sum(tree.right()) + tree.value()

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

    def insert_right(self, value):
        if self._right == None:
            self._right = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._right = self._right
            self._right = t

    def insert_left(self, value):
        if self._left == None:
            self._left = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._left = self._left
            self._left = t

