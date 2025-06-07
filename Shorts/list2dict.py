def list2dict(list2d):
    # your code here
    output = {}
    for row in list2d:
        output[row[0]] = row[1:]
    return output
