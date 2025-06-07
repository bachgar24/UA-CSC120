"""
    File: battleship.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From a guess and placement file, simulates a game of battleship.
    Assumes one entry on each line, with each guess is two integers split by a
    space, and each placement is one character followed by four integers split
    by spaces.
"""
from sys import *

class GridPos:
    """
        This class represents a coordinate position on a grid.

        The class defines:
            various getter and setter methods, 
            and a str() method.
        Requires a tuple coordinate argument on construction.
    """
    def __init__(self, coordinates):
        """
        constructor for GridPos objects; sets self._coordinates to 
        coordinates, creates self._ship to None, creates self._guessed to None

        Parameters:
            coordinates (tuple(int)): coordinate position of the object
        
        Returns:
            None
        """
        self._coordinates = coordinates
        self._ship = None
        self._guessed = False
        
    def coordinates(self):
        return self._coordinates
    
    def ship(self):
        return self._ship
    
    def set_ship(self, ship):
        self._ship = ship
        
    def guessed(self):
        return self._guessed
    
    def guess(self):
        self._guessed = True
        
    def __str__(self):
        if self._guessed:
            return "X"
        if self._ship != None:
            return str(self._ship)
        return "."

class Board:
    """
        This class represents a battleship board as a 2d list of GridPos.

        The class defines:
            a get_pos() method that returns a GridPos at a coordinate,
            a build_board() helper method that populates the Board with
            GridPos,
            an add_ship() method that adds a Ship to the dictionary of Ships,
            a guess() method that processes opposing players' guesses,
            and a str() method.
        Requires no arguments on construction.
    """
    def __init__(self):
        """
        constructor for Board objects; creates self._grid to an empty list,
        creates self._ships to an empty dict, then populates self._grid with 
        build_board().
        
        Parameters:
            None
        
        Returns:
            None
        """
        self._grid = []
        self._ships = dict()
        self.build_board()
    
    def get_pos(self, coordinates):
        """
        from a coordinate, finds and returns the corresponding GridPos

        Parameters:
            coordinates (tuple(int)): coordinate position to get

        Returns:
            GridPos: object at coordinates
        """
        return self._grid[coordinates[0]][coordinates[1]]
    
    def build_board(self):
        """
        helper method to populate the grid with GridPos, each with the proper
        indices/coordinates
        
        Parameters:
            None
        
        Returns:
            None
        """
        for i in range(10):
            self._grid.append([])
            for k in range(10):
                self._grid[i].append(GridPos((i, k)))
    
    def add_ship(self, ship):
        """
        adds a Ship to the Board's ships dict, the key being the Ship's symbol

        Parameters:
            ship (Ship): Ship to add
        
        Returns:
            None
        """
        self._ships[str(ship)] = ship
        
    def ships(self):
        return self._ships
    
    def guess(self, coordinates):
        """
        from coordinates, processes whether the guess was a hit, miss, or sunk
        the Ship, printing the result

        Parameters:
            coordinates (tuple(int)): coordinates to process guess for
        
        Returns:
            None
        """
        pos = self.get_pos(coordinates)
        ship = pos.ship()
        output = ""
        if pos.guessed():
            output = " (again)"
            
        # misses
        if ship == None:
            output = "miss" + output
            
        # hits
        else:
            output = "hit" + output
            ship.hit(coordinates)
        
            # check for sinked ship
            sunk = ship.sunk()
            if sunk:
                output = sunk
            
        pos.guess()
        print(output)
            
    
    def __str__(self):
        output = ""
        for row in self._grid[::-1]:
            for pos in row:
                output += str(pos)
            output += "\n"
            
        return output.strip()

class Ship:
    """
        This class represents a battleship ship.

        The class defines:
            an add_pos() helper method that adds the Ship to a GridPos and
            vice versa,
            a mass_add_pos() method that processes adding all GridPos from a
            start and end coordinate,
            a hit() method that represents when a Ship is hit,
            a sunk() method that checks if the Ship sank, returning a message,
            and a str() method.
        Requires a string model argument on construction.
    """
    def __init__(self, model):
        """
        constructor for Ship objects; sets self._model to model, creates 
        self._size and self._hits to 1, and creates self._pos to an empty dict

        Parameters:
            model (str): model of the ship as one char
        
        Returns:
            None
        """
        self._model = model
        self._size = 1
        self._hits = 1
        self._pos = dict()
        
    def set_size(self, size):
        self._size, self._hits = size, size
        
    def add_pos(self, coordinates, grid, line):
        """
        finds the GridPos at coordinates, then adds the Ship to it and it to
        the Ship's _pos dict

        Parameters:
            coordinates (tuple(int)): coordinates of position to add
            grid (Board): Board to add the Ship to
            line (str): line from input file to be printed in case of errors
        
        Returns:
            None
        """
        if coordinates < (0, 0) or coordinates > (9, 9):
            print("ERROR: ship out-of-bounds: " + line)
            exit(0)
            
        pos = grid.get_pos(coordinates)
        
        if pos.ship() != None:
            print("ERROR: overlapping ship: " + line)
            exit(0)
            
        self._pos[coordinates] = pos
        pos.set_ship(self)
        
    def mass_add_pos(self, start, end, grid, line):
        """
        iterates through every coordinate from start to end, calling add_pos()
        to add that GridPos to the Ship

        Parameters:
            start (tuple(int)): coordinate to start iterating
            end (tuple(int)): coordinate to end iterating
            grid (Board): Board to add the Ship to
            line (str): line from input file to be printed in case of errors

        Returns:
            int: the size of the ship
        """
        if start[0] != end[0] and start[1] != end[1]:
            print("ERROR: ship not horizontal or vertical: " + line)
            exit(0)
        
        counter = 0
        # horizontal ship
        for x in range(start[0], end[0] + 1):
            self.add_pos((x, start[1]), grid, line)
            counter += 1
        
        # vertical ship
        for y in range(start[1] + 1, end[1] + 1):
            self.add_pos((start[0], y), grid, line)
            counter += 1
            
        return counter
            
    def hit(self, coordinates):
        """
        registers a hit on the coordinate of the Ship, decreasing hits
        remaining

        Parameters:
            coordinates (tuple(int)): coordinate of GridPos hit
        
        Returns:
            None
        """
        pos = self._pos[coordinates]
        if pos.guessed():
            return
        self._hits -= 1
        
    def sunk(self):
        """
        checks if the Ship sank, and returns a message if so
        
        Parameters:
            None

        Returns:
            str: Ship sunk message
        """
        if self._hits > 0:
            return ""
        return "{} sunk".format(self)
    
    def __str__(self):
        return self._model

def read_placement(filename, grid):
    """
    reads the placements of Ships from the file, populating grid with them

    Parameters:
        filename (str): path to placement file
        grid (Board): Board to add Ships to
        
    Returns:
        None
    """
    file = open(filename)
    # dict of valid Ships for error checking on the inputs
    ships = {"A":5, "B":4, "S":3, "D":3, "P":2}
    for line in file:
        ship_info = line.split()
        ship = Ship(ship_info[0])
        start = (int(ship_info[1]), int(ship_info[2]))
        end = (int(ship_info[3]), int(ship_info[4]))
        
        if str(ship) not in ships or len(ships) < 1:
            print("ERROR: fleet composition incorrect")
            exit(0)
            
        # always make start the lower pair
        if start > end:
            temp = start
            start = end
            end = temp
            
        size = ship.mass_add_pos(start, end, grid, line)
        
        if ships[str(ship)] != size:
            print("ERROR: incorrect ship size: " + line)
            exit(0)
            
        ship.set_size(size)
        grid.add_ship(ship)
        ships.pop(str(ship))
        
    file.close()
    
    if len(ships) > 0:
        print("ERROR: fleet composition incorrect")
        exit(0)
        
    return

def read_guesses(filename, grid):
    """
    reads the guesses from the guess file, executing them on grid

    Parameters:
        filename (str): path to guess file
        grid (Board): Board to guess on
        
    Returns:
        None
    """
    file = open(filename)
    for line in file:
        # skip blank lines
        if line.strip() == "":
            continue
        
        guess = line.split()
        coordinates = (int(guess[0]), int(guess[1]))
        
        if coordinates < (0, 0) or coordinates > (9, 9):
            print("illegal guess")
            continue
        
        grid.guess(coordinates)
    file.close()
    return

def main():
    board = Board()
    read_placement(input(), board)
    read_guesses(input(), board)
    for ship in board.ships().values():
        if not ship.sunk():
            break
    else:
        print("all ships sunk: game over")
main()