def canonicalize_date(date_str):
    #put your code here
    for seperator in "-/ ":
        date_list = date_str.split(seperator)
        if len(date_list) == 3:
            break
        
    if len(date_list[2]) == 4:
        date_list.insert(0, date_list.pop(2))
        
    if len(date_list[1]) == 3:
        date_list[1] = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec").index(date_list[1]) + 1
    
    return "{:d}-{:d}-{:d}".format( int(date_list[0] ), int(date_list[1]), int(date_list[2]))