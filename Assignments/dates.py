"""
    File: dates.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: From an input file, reads dates and corresponding events on lines
    starting with "I" or prints all events for a date on lines starting with
    "R". Assumes all lines follow this format, as well as dates being in 
    yyyy-mm-dd, mm/dd/yyyy or mmm dd yyyy format with a colon to seperate 
    dates and events.
"""

class Date:
    """
        This class represents a date and its corresponding events.

        The class defines a str() method and an add_event() method that adds to
        the event list. Date strings are assumed to be in the canonicized 
        format in order to be standardized across Date objects. Requires one
        string event on construction.
    """

    def __init__(self, date_str, event):
        """
        constructor for Date objects, initializes name of the date and creates
        a list to contain all events
        
        Parameters:
            date_str (str): canonicized date 
            event (str): inital event to add
            
        Returns: 
            None
        """
        self._date_str = date_str
        self._event = [event]
        
    def get_date_str(self):
        return self._date_str
    
    def get_event(self):
        return self._event
    
    def add_event(self, event): 
        """
        appends an event and sorts the resulting list

        Parameters:
            event (str): event to add
            
        Returns:
            None
        """
        self._event.append(event)
        self._event.sort()
        
        
    def __str__(self):
        output = ""
        for event in self._event:
            output += "{}: {}\n".format(self._date_str, event)
        # returns each event on a new line
        return output[:-1]

class DateSet:
    """
        This class represents a collection that contains Date objects

        The class defines an add_date() method, which creates and adds Date
        objects to the collection, and a str() method. Date strings are mapped
        to the corresponding Date objects. Requires no parameters on
        construction, though add_date() requires a string date and an event.
    """

    def __init__(self):
        """
        creates an empty dictionary to hold Date objects
        
        Parameters:
            None
            
        Returns: 
            None
        """
        self._date_dict = {}
        
    def add_date(self, date_str, event):
        """
        creates new Date objects if needed and adds them to the dictionary,
        otherwise adds the event to an existing Date object

        Parameters:
            date_str (str): canonicized date 
            event (str): event to add
            
        Returns:
            None
        """
        if date_str not in self._date_dict:
            self._date_dict[date_str] = Date(date_str, event)
            
        else:
            self._date_dict[date_str].add_event(event)
    
    def get_date_dict(self):
        return self._date_dict
    
    def __str__(self):
        output = ""
        for date in self._date_dict.values():
            output += str(date)
        return output


def canonicalize_date(date_str):
    """
    converts various date formats into canonicized yyyy dd mm format

    Parameters:
        date_str (str): non-canonicized date 

    Returns:
        str: canonicized date
    """
    # changes raw str into list of 3 dates
    for seperator in "-/ ":
        date_list = date_str.split(seperator)
        if len(date_list) == 3:
            break
        
    # converts formats ending in year to year, day, month format
    if len(date_list[2]) == 4:
        date_list.insert(0, date_list.pop(2))
    
    # fixes word format months into ints
    if len(date_list[1]) == 3:
        date_list[1] = (("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                        "Aug", "Sep", "Oct", "Nov", "Dec")
                        .index(date_list[1]) + 1)
    
    return "{:d}-{:d}-{:d}".format(int(date_list[0]), int(date_list[1]),
                                   int(date_list[2]))

def read_data(date_set):
    """
    reads dates and events from a file, either adding to the DateSet or
    printing all events for that date. Illegal operations result in a 
    printed error message

    Parameters:
        date_set (DateSet): object that has a collection of Date objects
    
    Returns:
        None
    """
    file = open(input())
    for line in file:
        info = line[1:]
        # changes date str to canonicized version; space to prevent [:-1] trim
        date_str = canonicalize_date((info + " ")[:info.find(":")].strip())
        # add date and event to date dict
        if line[0] == "I":
            date_set.add_date(date_str, info[info.find(":") + 1:].strip())
            
        # print all events for the date
        elif line[0] == "R" and date_str in date_set.get_date_dict():
            print(date_set.get_date_dict()[date_str])
            
        elif line[0] != "R":
            print("Error - Illegal operation.")
            
    file.close()
    
def main():
    read_data(DateSet())
    
main()