directions = [(0,1), (1,0), (-1,0), (0, -1)]
data_file = "data.txt"


with open(data_file) as f:
    data = f.readlines()

grid = []
for i,line in enumerate(data):
    grid.append([])
    for j, l in enumerate(line.strip()):
        if l == "S":
            starting_pos = (i, j)
        grid[i].append(l)

cache = {}
end_blocks = {}

total_steps = 458

def compute_position(x, y, steps):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "#":
        return
    
    if steps == total_steps:
        end_blocks[(x,y)] = True
        cache[(x, y, steps)] = True
        return
    

    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        new_steps = steps + 1

        if (new_x, new_y, new_steps) not in cache:
            compute_position(new_x, new_y, new_steps)

    cache[(x, y, steps)] = True


compute_position(starting_pos[0], starting_pos[1], 0)

print(len(end_blocks.keys()))

