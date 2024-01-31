converter = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

area = 0
border = 0
starting_pos = (0,0)

current_pos = starting_pos

for line in data:
    _, _, hexcode = line.strip().split()
    direction = hexcode[-2]


    units = 0
    power = 0

    for i in range(len(hexcode) - 3, 1, -1):
        if hexcode[i].isdigit():
            digit = int(hexcode[i])
        else:
            digit = converter[hexcode[i]]
        units += int(digit*(16 ** power))
        power += 1
   
    if direction == "3":
        next_pos = (current_pos[0] - units, current_pos[1])
    elif direction == "1":
        next_pos = (current_pos[0] + units, current_pos[1])
    elif direction == "2":
        next_pos = (current_pos[0], current_pos[1] - units)
    elif direction == "0":
        next_pos = (current_pos[0], current_pos[1] + units)

    border += units
    area += (current_pos[0] * next_pos[1]) - (current_pos[1] * next_pos[0])

    current_pos = next_pos

interior = (abs(area)/2) - (border/2) + 1

print(border + interior)