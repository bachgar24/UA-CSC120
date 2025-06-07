"""
    File: pokemon.py
    Author: Garrett Bachman
    Course: CSC 120, Spring 2025
    Purpose: compiles data from CSV files, printing the pokemon type with the
    highest averages of each stat column based on repeatable user input
"""

def read_data():
    """
    compiles data from inputted CSV to find total stats and average values of 
    each pokemon type

    Parameters:
        None

    Returns:
        tup(dict{str:{str:list[int]}}, list[str]): calculated totals and 
        averages for each type, and column titles
    """
    file = open(input())
    # {"type":{"total":[stats], "avg":[stats]},...}
    poke_dict = {}
    header = file.readline().split(",")[4:-2]
    for line in file:
        # #,Name,Type1,Type2,Total,HP,Atk,Def,Sp.Atk,Sp.Def,Spd,Gen,Leg
        temp = line.split(",")
        type, stats = temp[2], temp[4:-2]

        # add type to dict
        if type not in poke_dict:
            poke_dict[type] = {"total":[0]*(len(stats)+1), "avg":[]}

        # add stats to total, and count iterations
        for i in range(len(stats)):
            poke_dict[type]["total"][i] += int(stats[i])
        
        poke_dict[type]["total"][-1] += 1
    file.close()
    
    # find averages
    for val in poke_dict.values():
        count, total, avg = val["total"][-1], val["total"][:-1], val["avg"]

        for sum in total:
            avg.append(sum/count)

    return poke_dict, header


def highest_average(poke_dict, header):
    """
    finds the highest average types for each stat, sorted alphabetically

    Parameters:
        poke_dict (dict{str:{str:list[int]}}): calculated stats for each type
        header (list[str]): list of column titles

    Returns:
        dict{str:list[tup(str, float)]}: highest average stats mapped to types 
    """
    # {"stat":[("type", avg),...],...}
    avg_dict = {}
    for i in range(len(header)):
        type = [("", 0)]
        for k, v in poke_dict.items():
            avg = v["avg"][i]
            # replace if larger average, add to list if equal
            if avg > type[0][1]:
                type = [(k, avg)]

            elif avg == type[0][1]:
                type.append((k, avg))

        avg_dict[header[i]] = sorted(type)
    return avg_dict

def find_stats(avg_dict, query):
    """
    converts query into formatted output line with respective information

    Parameters:
        avg_dict (dict{str:list[tup(str, float)]}): highest average stats
        mapped to types
        query (str): inputted user query

    Returns:
        str: each resulting type and their average values
    """
    output = ""
    for type, stats in avg_dict[query]:
        output += "{}: {}\n".format(type, stats)

    # trim whitespace at end
    return output[:-1]

def fix_query(query):
    """
    fixes variance in mixed capitalization between files and queries 

    Parameters:
        query (str): inputted user query

    Returns:
        str: query with fixed syntax or original if no change is needed
    """
    fix_dict = {"Specialattack":"Sp. Atk", "Specialdefense":"Sp. Def",
                    "Hp":"HP"}
    
    if query in fix_dict:
        return fix_dict[query]
    
    return query

def run_query(avg_dict):
    """
    main loop, accepts queries that fit valid stats and breaking on new line

    Parameters:
        avg_dict (dict{str:list[tup(str, float)]}): highest average stats
        mapped to types
    
    Returns:
        None
    """
    while True:
        query = input().capitalize()
        if query == "":
            break

        # fixes issues with Sp. stats and HP
        query = fix_query(query)

        if query not in avg_dict:
            continue

        print(find_stats(avg_dict, query))

def main():
    run_query(highest_average(*read_data()))

main()