"""
    File: bball.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From an input file, reads teams, creating Team objects and adding
    to the ConferenceSet object, then prints highest average scoring 
    Conferences. Assumes all lines follow "name (conf) wins losses" format,
    skipping lines that start with a #.
"""

class Team:
    """
        This class represents a team and its corresponding name, conference, 
        and scores.

        The class defines a str() method and a win_ratio() method that returns
        the Team's win/loss ratio. Lines sent to the constructor are assumed 
        to follow the "name (conf) wins losses" format, requiring one line on
        construction.
    """
    def __init__(self, line):
        """
        constructor for Team objects, initializes name of the team, its 
        conference, as well as its wins and losses as ints
        
        Parameters:
            line (str): line entry of a team
        
        Returns:
            None
        """
        scores = line[line.rfind(")") + 1:].split()
        self._name = line[:line.rfind("(")].strip()
        self._conf = line[line.rfind("(") + 1:line.rfind(")")]
        self._wins = int(scores[0])
        self._losses = int(scores[1])
    
    def name(self):
        return self._name
    
    def conf(self):
        return self._conf
    
    def win_ratio(self):
        """
        returns the win ratio for the team

        Parameters:
            None
            
        Returns:
            float: win ratio
        """
        return self._wins / (self._losses + self._wins)
    
    def __str__(self):
        return "{} : {}".format(self._name, str(self.win_ratio()))

class Conference:
    """
        This class represents a conference and the Teams belonging to that
        conference.

        The class defines a str() method, a contains() method if that team is
        in the conference, a lt() method that determines alphabetical order of
        Conferences, an add() method that adds a team to the conference, and a
        win_ratio_avg() method that returns the Conference's Teams' average 
        win ratio. Requires only the name of the conference as a string on
        construction.
    """
    def __init__(self, conf): 
        """
        constructor for Conference objects, initializes name of the conference
        and creates a list to contain all teams

        Parameters:
            conf (str): name of the conference
            
        Returns:
            None
        """
        self._name = conf
        self._teams = []
        
    def __contains__(self, team):
        """
        checks if team is in this Conference's Teams

        Parameters:
            team (Team): Team object to check

        Returns:
            bool: if the team is in this Conference
        """
        return team in self._teams
    
    def __lt__(self, other):
        """
        determines alphabetical order of two teams for sorted()

        Parameters:
            other (Conference): Conference object to check

        Returns:
            bool: if this Conference's name is first alphabetically
        """
        return self.name() < other.name()
    
    def name(self):
        return self._name
    
    def add(self, team):
        """
        appends team to the list of Teams

        Parameters:
            team (Team): Team object to add
            
        Returns:
            None
        """
        self._teams.append(team)
        
    def win_ratio_avg(self): 
        """
        returns the average win ratio for the Conference
        
        Parameters:
            None

        Returns:
            float: average win ratio of all Teams
        """
        output = 0
        for team in self._teams:
            output += team.win_ratio()
        return output / len(self._teams)
    
    def __str__(self): 
        return "{} : {}".format(self._name, str(self.win_ratio_avg()))

class ConferenceSet:
    """
        This class represents a collection of Conferences.

        The class defines a str() method, an add() method that adds a team to
        the Confernce list, and a best() method that returns the highest
        scoring Conferences in the list. Requires no arguments on construction
    """
    def __init__(self):
        """
        constructor for ConferenceSet objects, creates an empty list of 
        conferences
        
        Parameters:
            None

        Returns:
            None
        """
        self._confs = []
    
    def add(self, team):
        """
        adds team to the appropriate Conference in the list of Conferences, if
        necessary creating a Conference object for the Conference of this Team

        Parameters:
            team (Team): Team object to add
            
        Returns:
            None
        """
        conf = team.conf()
        for conf_obj in self._confs:
            if conf_obj.name() == conf:
                conf_obj.add(team)
                return
            
        conf = Conference(team.conf())
        conf.add(team)
        self._confs.append(conf)
        
    def best(self):
        """
        returns a list of Conferences that have the highest average win ratio
        in the ConferenceSet
        
        Parameters:
            None

        Returns:
            list[Conference]: sorted, highest scoring Conferences
        """
        output = []
        for conf in self._confs:
            if (len(output) != 0 
                and output[0].win_ratio_avg() < conf.win_ratio_avg()):
                output.clear()
                
            if (len(output) == 0 
                or output[0].win_ratio_avg() == conf.win_ratio_avg()):
                output.append(conf)
                
        return sorted(output)
    
def main():
    file = open(input())
    confs = ConferenceSet()
    
    for line in file:
        if line[0] == "#":
            continue
        confs.add(Team(line))
    
    for conf in confs.best():
        print(conf)
        
    file.close()

main()