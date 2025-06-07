"""Implement your class here"""
class Word:
    def __init__(self, word):
        self._word = word
        
    def __len__(self):
        return len(str(self._word))
        
    def __str__(self):
        return self._word.lower()
        
    def __eq__(self, other):
        if len(other) != len(self._word):
            return False
            
        temp = list(str(self._word))
        print(temp, str(self), str(other), sep="\n")
        for char in str(other):
            if char not in temp:
                return False
                
            temp.remove(char)
            
        return True
    
def test05():
    w1 = Word("Hi there!")
    w2 = Word("Hit here!")
    return w1 == w2
print(test05())