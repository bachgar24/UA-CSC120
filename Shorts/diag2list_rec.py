def diag2list_rec(grid):
    return diag_helper(grid, 0)
    
def diag_helper(grid, i):
    if grid == []:
        return []
    output = [grid[i][i]]
    if len(grid) == i+1:
        return output
    output.extend(diag_helper(grid, i+1))
    return output