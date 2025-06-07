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

def decimal2binary(n):
    #Your code goes here
    remainders = Stack()
    num = n
    while num != 0:
        remainders.push(num % 2)
        num //= 2
    output = ""
    while not remainders.is_empty():
        output += str(remainders.pop())
    return output
