data_file = "data.txt"

with open(data_file, "r") as f:
    lines = f.readlines()

grid = []

for line in lines:
    clean_line = list(line.strip())
    grid.append(clean_line)

# Part 1

def is_part_number(start_x, start_y, end_x, end_y, digit):
    start_x = start_x if start_x >= 0 else 0
    start_y = start_y if start_y >= 0 else 0
    end_x = end_x + 1 if end_x < len(grid) else len(grid)
    end_y = end_y + 1 if end_y < len(grid[0]) else len(grid[0])
    # print(start_x, start_y, end_x, end_y)
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if not grid[i][j].isdigit() and grid[i][j] != ".":
                if grid[i][j] == "*":
                    if not cogs.get((i,j)):
                        cogs[(i,j)] = {
                            "digits": 0,
                            "gear_ratio": 1
                        }
                    cogs[(i,j)]["digits"] += 1
                    cogs[(i,j)]["gear_ratio"] *= digit
                return True
            
    return False


sum_numbers = 0

i = 0

# Part 2
cogs = {}
while i < len(grid):
    j = 0
    while j < len(grid[i]):
        if grid[i][j].isdigit():
            digit = grid[i][j]

            start_x = j - 1
            start_y = i - 1

            j += 1
            while j < len(grid[i]) and grid[i][j].isdigit():
                digit += grid[i][j]
                j += 1
            
            end_x = j
            end_y = i + 1

            if is_part_number(start_x, start_y, end_x, end_y, int(digit)):
                sum_numbers += int(digit)
        else:
            j += 1
    i += 1

print(sum_numbers)

sum_cogs = 0
for pos in cogs:
    if cogs[pos]["digits"] == 2:
        sum_cogs += cogs[pos]["gear_ratio"]

print(sum_cogs)