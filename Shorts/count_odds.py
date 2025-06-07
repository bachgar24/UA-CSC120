def count_odds(alist):
    #Your code goes here
    if alist == []:
        return 0
    return int(alist[0] % 2) + count_odds(alist[1:])