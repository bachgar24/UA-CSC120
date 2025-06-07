def column2list_rec(grid, n):
    if grid == []:
        return []
    output = [grid[0][n]]
    if len(grid) == 1:
        return output
    output.extend(column2list_rec(grid[1:], n))
    return output