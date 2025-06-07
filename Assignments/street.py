"""
    File: street.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From an inputted string, decodes it and prints a representation
    of the string described, out of buildings, parks, and empty lots. Assumes
    each entry is seperated by spaces, with the format 
    "[type]:[params],[params]". Only entries starting with "b", "p", and "e"
    are considered, and only the first few parameters are considered depending
    on the type declared.
"""

class Building:
    """
        This class represents a building to be used in the printable street
        scene.

        The class defines:
            an at_height() method that returns the string representaion of the
            Building at a certain height.
        Requires an int width and height, as well as a string brick on
        construction.
    """
    def __init__(self, width, height, brick):
        """
        constructor for Building objects; sets _width to width, sets _height
        to height, and sets _brick to brick

        Parameters:
            width (int): width of the Building
            height (int): height of the Building
            brick (str): character used to represent Building in the street
            
        Returns:
            None
        """
        self._width = width
        self._height = height
        self._brick = brick
        
    def at_height(self, height):
        """
        for a height, creates and returns a string of Building at that height.
        If height exceeds Building's height, returns a string of whitespace

        Parameters:
            height (int): level of the street to create representation for

        Returns:
            str: representaion of Building at height
        """
        if height >= self._height:
            return " " * self._width
        
        return self._brick * self._width

class Park:
    """
    This class represents a park to be used in the printable street scene.
    
        The class defines:
            an at_height() method that returns the string representaion of the
            Park at a certain height.
        Requires an int width, as well as a string foliage on construction.
    """
    def __init__(self, width, foliage):
        """
        constructor for Park objects; sets _width to width, sets _foliage to
        foliage, and creates _height to 5

        Parameters:
            width (int): width of the Park
            foliage (str): character used to represent Park's foliage levels
            in the street
            
        Returns:
            None
        """
        self._width = width
        self._foliage = foliage
        self._height = 5
        
    def at_height(self, height):
        """
        for a height, creates and returns a string of Park at that height. If
        height exceeds Park's height, returns a string of whitespace

        Parameters:
            height (int): level of the street to create representation for

        Returns:
            str: representaion of Park at height
        """
        if height >= self._height:
            return " " * self._width
        
        if height < 2:
            edge = " " * (self._width//2)
            return edge + "|" + edge
        
        foliage = self._foliage * (-2 * height + 4 + self._height)
        edge = " " * ((self._width - len(foliage))//2)
        return edge + foliage + edge

class EmptyLot:
    """
        This class represents an empty lot to be used in the printable street
        scene.

        The class defines:
            a fix_underscores() method that replaces underscores with 
            whitespace,
            and an at_height() method that returns the string representaion of
            the EmptyLot at a certain height.
        Requires an int width, as well as a string trash on construction.
    """
    def __init__(self, width, trash):
        """
        constructor for EmptyLot objects; sets _width to width, sets _trash to
        return of trash from fix_underscores(), and creates _height to 1

        Parameters:
            width (int): width of the EmptyLot
            trash (str): character used repetitively to represent EmptyLot in
            the street
            
        Returns:
            None
        """
        self._width = width
        self._trash = self.fix_underscores(trash)
        self._height = 1
        
    def fix_underscores(self, trash):
        """
        replaces all instances of underscores in trash with whitespace

        Parameters:
            trash (str): string to replace underscores of

        Returns:
            str: new string with underscores replaced
        """
        if trash == "":
            return ""
        
        if trash[0] == "_":
            return " " + self.fix_underscores(trash[1:])
        
        return trash[0] + self.fix_underscores(trash[1:])
    
    def at_height(self, height):
        """
        for a height, creates and returns a string of EmptyLot at that height.
        If height exceeds EmptyLot's height, returns a string of whitespace

        Parameters:
            height (int): level of the street to create representation for

        Returns:
            str: representaion of EmptyLot at height
        """
        if height >= self._height:
            return " " * self._width
        
        reps = self._width//len(self._trash)
        excess = self._width % (reps * len(self._trash))
        return self._trash * reps + self._trash[:excess]

def construct_street(street):
    """
    uses street elements to create corresponding street objects in a new list

    Parameters:
        street (list[str]): list of string instructions for each object

    Returns:
        list: list of street objects created to specifications
    """
    if street == []:
        return []
    
    type, params = street[0][0], street[0][2:].split(",")
    if type == "b":
        output = Building(int(params[0]), int(params[1]), params[2])
        
    elif type == "p":
        output = Park(int(params[0]), params[1])
        
    elif type == "e":
        output = EmptyLot(int(params[0]), params[1])
        
    return [output] + construct_street(street[1:])

def print_street(street):
    """
    calls helper functions to return every level of street as one string, then
    adds borders and prints

    Parameters:
        street (list[]): list of street objects

    Returns:
        None
    """
    middle = print_street_helper(street, 0)
    sides = "+" + (len(print_street_at_height(street, 0))) * "-" + "+"
    print(sides + "\n" + middle + "\n" + sides)
    
def check_empty(line):
    """
    checks if a string consists of only whitespace or is empty

    Parameters:
        line (str): string to check

    Returns:
        bool: if line has only whitespace
    """
    if line == "":
        return True
    
    if line[0] == " ":
        return check_empty(line[1:])
    
    return False

def print_street_helper(street, height):
    """
    calls for strings of each level of street until height exceeds the height
    of every object in street, then returns the result

    Parameters:
        street (list[]): list of street objects
        height (int): level of street to get

    Returns:
        str: string representation of street, without top and bottom borders
    """
    line = "|" + print_street_at_height(street, height) + "|"
    if check_empty(line[1:-1]):
        return line
    
    return print_street_helper(street, height + 1) + "\n" + line

def print_street_at_height(street, height):
    """
    compiles every element in street's representations at height

    Parameters:
        street (list[]): list of street objects
        height (int): level of street to get representations of

    Returns:
        str: string representation of street at height
    """
    if street == []:
        return ""
    
    return (street[0].at_height(height)
           + print_street_at_height(street[1:], height))
    
def main():
    print_street(construct_street(input("Street: ").split()))
    
main()