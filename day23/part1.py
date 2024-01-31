import sys

sys.setrecursionlimit(10000)
directions = [(0,1), (1,0), (0, -1), (-1, 0)]

slopes = {
    "<": (0,-1),
    "v": (1,0),
    ">": (0, 1),
    "^": (-1, 0)
} 

def dfs(x, y, steps, visited):
    if x < 0 or x >= len(grid):
        return 0
    
    if y < 0 or y >= len(grid[0]):
        return 0
    
    visited.append((x,y))
    if (x,y) == finish:
        return steps
    
    if grid[x][y] in slopes:
        d = slopes[grid[x][y]]
        return dfs(x + d[0], y + d[1], steps + 1, list(visited))
    
    max_steps = 0
    for d in directions:
        if grid[x + d[0]][y + d[1]] != "#" and (x + d[0], y + d[1]) not in visited:
            if grid[x + d[0]][y + d[1]] not in slopes or slopes[grid[x + d[0]][y + d[1]]] == d:
                dir_steps = dfs(x + d[0], y + d[1], steps + 1, list(visited))
                if dir_steps > max_steps:
                    max_steps = dir_steps
    
    return max_steps

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

grid = []
for i, line in enumerate(data):
    grid.append([])
    for j, c in enumerate(line.strip()):
        grid[i].append(c)

        if c == ".":
            if i == 0:
                starting_pos = (i, j)
            if i == len(data) - 1:
                finish = (i, j)

print(dfs(starting_pos[0], starting_pos[1], 0, []))