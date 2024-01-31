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

starting_positions = []

for i in range(rows):
    starting_positions.append({
        "position": (i, 0),
        "direction": (0, 1)
    })
    starting_positions.append({
        "position": (i, cols - 1),
        "direction": (0, -1)
    })

    if i == 0 or i == rows - 1:
        for j in range(1, cols - 1):
            move_dir = 1 if i == 0 else -1

            starting_positions.append({
                "position": (i, j),
                "direction": (move_dir, 0)
            })

max_e = 0

for sp in starting_positions:
    q = deque()

    q.append(sp)
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

    max_e = max(max_e, total_energized)

print(max_e)
