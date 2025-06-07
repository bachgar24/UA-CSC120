"""implement your class here"""
class Temp:
    def __init__(self, temp, unit):
        self._temp = temp
        self._unit = unit
        
    def __str__(self):
        return str(self._temp) + self._unit
    
    def get_unit(self):
        return self._unit
    
    def get_temp(self):
        return self._temp
        
    def c_to_f(temp):
        if (temp.get_unit() == "C"):
            return temp.get_temp() * 9.0/5.0 + 32
        return temp.get_temp()
        
    def __eq__(self, other):
        return self.c_to_f() == other.c_to_f()
        
    def __gt__(self, other):
        return self.c_to_f() > other.c_to_f()
    
    def __ge__(self, other):
        return self.c_to_f() >= other.c_to_f()
        
    def __lt__(self, other):
        return self.c_to_f() < other.c_to_f()
        
    def __le__(self, other):
        return self.c_to_f() <= other.c_to_f()
        
    def __ne__(self, other):
        return self.c_to_f() != other.c_to_f()






"""DO NOT MODIFY ANYTHING BELOW THIS LINE"""
def test01():
    t1 = Temp(0, "C")
    t2 = Temp(32, "F")
    return t1 == t2

def test02():
    t1 = Temp(0, "C")
    t2 = Temp(0, "F")
    return t1 > t2
    
def test03():
    t1 = Temp(100, "C")
    t2 = Temp(212, "F")
    return t1 != t2

def test04():
    t1 = Temp(100, "C")
    return str(t1)
    
def test05():
    t1 = Temp(53, "F")
    return str(t1)

def test06():
    t1 = Temp(100,"C")
    return t1 == t1
    
def test07():
    t1 = Temp(100,"C")
    return t1 > t1
    

def temps(test_num):
    test_func = globals()['test{0}'.format(test_num)]
    return test_func()