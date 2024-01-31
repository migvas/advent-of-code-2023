from collections import deque

data_file = "data.txt"
mirrors = {}
splitters = {}
rows = 0
cols = 0
with open(data_file) as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        for idx, c in enumerate(line):
            if c == "-" or c == "|":
                splitters[(rows, idx)] = c
            elif c == "\\" or c == "/":
                mirrors[(rows, idx)] = c


        rows += 1

        if not cols:
            cols = len(line)

q = deque()

starting_pos = {
    "position": (0,0),
    "direction": (0,1)
}

q.append(starting_pos)

energized_tiles = {}

total_energized = 0

while q:
    beam = q.popleft()
    pos = beam["position"]
    direction = beam["direction"]
    if pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols:
        if not energized_tiles.get(pos):
            total_energized += 1
            energized_tiles[pos] = [direction]
        else:
            if direction in energized_tiles[pos]:
                continue
            
            energized_tiles[pos].append(dir)
        
        if splitters.get(pos):
            if splitters[pos] == "-" and direction[0]:
                q.append({
                    "position": (pos[0], pos[1] + 1),
                    "direction": (0, 1)
                })
                q.append({
                    "position": (pos[0], pos[1] - 1),
                    "direction": (0, -1)
                })
            
            elif splitters[pos] == "|" and direction[1]:
                q.append({
                    "position": (pos[0] + 1, pos[1]),
                    "direction": (1, 0)
                })
                q.append({
                    "position": (pos[0] - 1, pos[1]),
                    "direction": (-1, 0)
                })
            else:
                q.append({
                    "position": (pos[0] + direction[0], pos[1] + direction[1]),
                    "direction": direction
                })

        elif mirrors.get(pos):
            if mirrors[pos] == "/":
                q.append({
                    "position": (pos[0] - direction[1], pos[1] - direction[0]),
                    "direction": (-direction[1], -direction[0])
                })
            elif mirrors[pos] == "\\":
                q.append({
                    "position": (pos[0] + direction[1], pos[1] + direction[0]),
                    "direction": (direction[1], direction[0])
                })

        else:
            q.append({
                    "position": (pos[0] + direction[0], pos[1] + direction[1]),
                    "direction": direction
                })
            
print(total_energized)