class Queue:
    def __init__(self):
        self._items = ""

    def enqueue(self, item):
        self._items += item

    def dequeue(self):
        if self._items == "":
            return
        
        popped, self._items = self._items[0], self._items[1:]
        return popped
    
    def is_empty(self):
        return self._items == ""

    def __str__(self):
        return self._items
    
#Do not modify anything below this line
def test01():
    q = Queue()
    for c in "abcd":
        q.enqueue(c)
    return str(q)

def test02():
    q = Queue()
    for c in "abcd":
        q.enqueue(c)
    q.dequeue()
    return q.dequeue()
def test03():
    q = Queue()
    for c in "abcd":
        q.enqueue(c)
    q.dequeue()
    q.dequeue()
    return q.is_empty()

def test04():
    q = Queue()
    for c in "hide":
        q.enqueue(c)
    q.dequeue()
    q.dequeue()
    q.enqueue("e")
    q.enqueue("p")
    return str(q)