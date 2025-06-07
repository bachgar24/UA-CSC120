def sum_odds(alist):
    # Your code goes here
    if alist == []:
        return 0
    elif alist[0] % 2 == 0:
        return sum_odds(alist[1:])
    return alist[0] + sum_odds(alist[1:])