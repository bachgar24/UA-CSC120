def invert_dict(origdict):
    # Your code goes here
    output = {}
    for key in origdict:
        output[origdict[key]] = key
        
    return output