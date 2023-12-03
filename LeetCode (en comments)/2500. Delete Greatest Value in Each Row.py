def delete_greatest_value(grid):
    answer = 0
    while len(grid[0]) > 0:
        choose = 0
        for arr in grid:
            choose = max(choose, arr.pop(arr.index(max(arr))))
        answer += choose
    return answer