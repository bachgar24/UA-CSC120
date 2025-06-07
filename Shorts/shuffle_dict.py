def shuffle_dict(somedict):
    # your code here
    shuffled_dict ={}
    sorted_keys = sorted(list(somedict.keys()))
    sorted_vals = sorted(list(somedict.values()))
    
    for i in range(len(sorted_keys)):
        shuffled_dict[sorted_keys[i]] = sorted_vals[i]
        
    return shuffled_dict