from collections import deque
data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

round_r = {}
cube_r = {}
q = deque()
max_load = len(data)

for i, line in enumerate(data):
    for j, r in enumerate(line.strip()):
        if r == "O":
            round_r[(i, j)] = True
            q.append((i,j))
        elif r == "#":
            cube_r[(i,j)] = True

total_load = 0

while q:
    r = q.popleft()
    l = r[0]
    round_r[r] = False
    while l >= 0 and not round_r.get((l, r[1])) and not cube_r.get((l, r[1])):
        l -= 1

    l += 1
    round_r[(l, r[1])] = True
    total_load += max_load - l

print(total_load)