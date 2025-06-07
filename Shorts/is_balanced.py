class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []
    
    def __str__(self):
        return str(self._items)



def is_balanced(symbols):
    # Your code goes here
    delim_stack = Stack()
    for char in symbols:
        for test in ("(", ")"), ("[", "]"), ("{", "}"):
            if not test_delims(char, test[0], test[1], delim_stack):
                return False
    return True

def test_delims(char, left, right, stack):
    if char == left:
        stack.push(char)
    elif char == right and (stack.is_empty() or stack.pop() != left):
        return False
    return True