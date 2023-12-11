from collections import deque


def is_iside(P, polygon):
    def is_between(p, a, b):
        return p >= a and p <= b or p <= a and p >= b

    inside = False
    i = len(polygon) - 1
    j = 0

    while j < len(polygon):
        A = polygon[i]
        B = polygon[j]
        if P[0] == A[0] and P[1] == A[1] or P[0] == B[0] and P[1] == B[1]:
            return 0
        if A[1] == B[1] and P[1] == A[1] and is_between(P[0], A[0], B[0]):
            return 0

        if is_between(P[1], A[1], B[1]):
            if P[1] == A[1] and B[1] >= A[1] or P[1] == B[1] and A[1] >= B[1]:
                i = j
                j += 1
                continue
            c = (A[0] - P[0]) * (B[1] - P[1]) - (B[0] - P[0]) * (A[1] - P[1])
            if not c:
                return 0
            if (A[1] < B[1]) == (c > 0):
                inside = not inside
        i = j
        j += 1
    return 1 if inside else -1


starting_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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
        (-1, 0): (0, -1)
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
            starting_pos = (i, j)

q = deque()
for sd in starting_directions:
    new_path = []
    new_path.append(starting_pos)
    q.append({
        "position": starting_pos,
        "direction": sd,
        "path": new_path,
        "minx": starting_pos[0],
        "miny": starting_pos[1],
        "maxx": starting_pos[0],
        "maxy": starting_pos[1]
    })

while 1:
    curr = q.popleft()

    current_pos = curr["position"]
    direction = curr["direction"]
    path = curr["path"]
    minx = curr["minx"]
    miny = curr["miny"]
    maxx = curr["maxx"]
    maxy = curr["maxy"]
    next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
        continue

    if grid[next_pos[0]][next_pos[1]] == 'S':
        break

    if not pipes.get(grid[next_pos[0]][next_pos[1]]):
        continue

    if not pipes[grid[next_pos[0]][next_pos[1]]].get(direction):
        continue

    path.append(next_pos)
    minx = min(minx, next_pos[0])
    miny = min(miny, next_pos[1])
    maxx = max(maxx, next_pos[0])
    maxy = max(maxy, next_pos[1])
    q.append({
        "position": next_pos,
        "direction": pipes[grid[next_pos[0]][next_pos[1]]][direction],
        "path": path,
        "minx": minx,
        "miny": miny,
        "maxx": maxx,
        "maxy": maxy
    })

inside_points = 0
print(minx, miny, maxx, maxy)
for i in range(minx, maxx + 1):
    for j in range(miny, maxy + 1):
        if is_iside((i, j), path) == 1:
            inside_points += 1

print(inside_points)
