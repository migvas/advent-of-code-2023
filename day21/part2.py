from collections import deque

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


for i in range(3):
    total_steps = (len(grid)//2) + len(grid) * i
    cache = {}
    end_blocks = 0

    q = deque()

    q.append((starting_pos[0], starting_pos[1], 0))
    cache[(starting_pos[0], starting_pos[1], 0)] = True

    while q:
        x, y, steps = q.popleft()

        grid_x = x % len(grid)
        grid_y = y % len(grid[0])

        if steps == total_steps:
            end_blocks += 1
            cache[(x, y, steps)] = True
            continue

        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            new_steps = steps + 1

            new_grid_x = new_x % len(grid)
            new_grid_y = new_y % len(grid[0])

            if (new_x, new_y, new_steps) not in cache and grid[new_grid_x][new_grid_y] != "#":
                cache[(new_x, new_y, new_steps)] = True
                q.append((new_x, new_y, new_steps))

    print(end_blocks)


# With the 3 computed values we can compute the quadratic formula for the relationship between number of steps and total blocks reached
# f(x) = ax^2 + bx + c and f(0) = 3755, f(1) = 33494 and f(2) = 92811
# a = 14789, b = 14950, c = 3755
# steps = len(grid) * x + (len(grid) // 2)
# So for 26501365 steps we need to compute f(202300)

print("Total blocks:")
print(14789 * (202300 ** 2) + 14950 * 202300 + 3755)