data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

area = 0
border = 0
starting_pos = (0,0)

current_pos = starting_pos

for line in data:
    direction, units, _ = line.strip().split()
    units = int(units)

   
    if direction == "U":
        next_pos = (current_pos[0] - units, current_pos[1])
    elif direction == "D":
        next_pos = (current_pos[0] + units, current_pos[1])
    elif direction == "L":
        next_pos = (current_pos[0], current_pos[1] - units)
    elif direction == "R":
        next_pos = (current_pos[0], current_pos[1] + units)

    border += units
    area += (current_pos[0] * next_pos[1]) - (current_pos[1] * next_pos[0])

    current_pos = next_pos

interior = (abs(area)/2) - (border/2) + 1

print(border + interior)