def ngram(arglist, startpos, length):
    # your code here
    if startpos + length > len(arglist):
        return []
    return arglist[startpos:length+startpos]