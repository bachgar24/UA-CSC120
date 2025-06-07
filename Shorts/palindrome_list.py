def palindrome_list(arglist):
    if arglist == []:
        return True
    if arglist[0] != arglist[-1]:
        return False
    return palindrome_list(arglist[1:-1])