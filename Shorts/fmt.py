def fmt(spec, values):
    if len(spec) < 2 or values == []:
        return spec
    
    if spec[:2] == "{}":
        return str(values[0]) + fmt(spec[2:], values[1:])
    
    return spec[:2] + fmt(spec[2:], values)   