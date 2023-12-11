data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

galaxies = []

lines = 0
max_col = 0
col_has_galaxy = {}
for line in data:
    line = list(line.strip())

    has_galaxy = False

    for i in range(len(line)):
        if line[i] == "#":
            galaxies.append([lines, i])
            col_has_galaxy[i] = True
            max_col = max(max_col, i)
            has_galaxy = True

    if not has_galaxy:
        lines += 1

    lines += 1

no_galaxy = []
for i in range(max_col):
    if not col_has_galaxy.get(i):
        no_galaxy.append(i)


for galaxy in galaxies:
    add_col = 0
    for c in no_galaxy:
        if galaxy[1] > c:
            add_col += 1
        else:
            break
    galaxy[1] += add_col

total_dist = 0

for idx1 in range(len(galaxies) - 1):
    for idx2 in range(idx1 + 1, len(galaxies)):
        distance = abs(galaxies[idx2][0] - galaxies[idx1][0]) + abs(galaxies[idx2][1] - galaxies[idx1][1])
        total_dist += distance

print(total_dist)