def str2objects(spec):
    if spec == "":
        return []
    
    split = spec.split(None, 1)
    
    if len(split) > 1:
        spec =  split[1]
    else: 
        spec = ""
        
    curr = split[0]
    
    if curr == "dict":
        curr = dict()
    
    elif curr == "list":
        curr = list()
        
    else:
        curr = ""
    
    return [curr] + str2objects(spec)