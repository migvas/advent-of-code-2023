from collections import deque

starting_directions = [(-1,0), (1,0), (0,-1), (0,1)]

pipes = {
    "|": {
        (1, 0): (1, 0),
        (-1, 0): (-1, 0)
    },
    "-": {
        (0, 1): (0, 1),
        (0, -1): (0, -1)
    },
    "L": {
        (1, 0): (0, 1),
        (0, -1): (-1, 0)
    },
    "J": {
        (0, 1): (-1, 0),
        (1, 0): (0, -1)
    },
    "7": {
        (0, 1): (1, 0),
        (-1,0): (0, -1)
    },
    "F": {
        (0, -1): (1, 0),
        (-1, 0): (0, 1)
    }
}

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()


grid = [list(line.strip()) for line in data]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            starting_pos = (i,j)

q = deque()
for sd in starting_directions:
    q.append({
        "position": starting_pos,
        "direction": sd,
        "steps": 0
    })

while 1:
    curr = q.popleft()
    
    current_pos = curr["position"]
    direction = curr["direction"]
    steps = curr["steps"]
    next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
        continue
    
    if grid[next_pos[0]][next_pos[1]] == 'S':
        print((steps + 1) // 2)
        break
    
    if not pipes.get(grid[next_pos[0]][next_pos[1]]):
        continue
    
    if not pipes[grid[next_pos[0]][next_pos[1]]].get(direction):
        continue
    
    q.append({
        "position": next_pos,
        "direction": pipes[grid[next_pos[0]][next_pos[1]]][direction],
        "steps": steps + 1
    })
