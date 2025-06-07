"""Implement your class here"""
class Color:
    
    def __init__(self, r, g, b):
        self._r = self.fix_values(r)
        self._g = self.fix_values(g)
        self._b = self.fix_values(b)
        
    def fix_values(self, color):
        if color < 0:
            return 0
            
        if color > 255:
            return 255
            
        return color
        
    def get_rgb(self):
        return self._r, self._g, self._b
        
    def remove_red(self):
        self._r = 0
    
    def __str__(self):
        return "Color({},{},{})".format(self._r, self._g, self._b)
    
    def __eq__(self, other):
        return self.get_rgb() == other.get_rgb()
    



"""DO NOT MODIFY ANYTHING BELOW THIS LINE"""
def test01():
    color1 = Color(50,100,140)
    return color1.get_rgb()
    
def test02():
    color1 = Color(50,100,140)
    return str(color1)

def test03():
    color1 = Color(135,50,140)
    color1.remove_red()
    return str(color1)

def test04():
    color1 = Color(50,100,140)
    color2 = Color(135,50,140)
    return color1 == color2

def test05():
    color1 = Color(65,100,180)
    color2 = Color(65,100,180)
    return color1 == color2
    
def test06():
    color1 = Color(255,255,255)
    color1.remove_red()
    return str(color1)

def test07():
    color1 = Color(255,255,255)
    color1.remove_red()
    return color1.get_rgb()
    
def test08():
    color1 = Color(50,100,140)
    return color1.get_rgb()[2]

def colors(test_num):
    test_func = globals()['test{0}'.format(test_num)]
    return test_func()