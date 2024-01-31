data_file = "data.txt"

with open(data_file, "r") as f:
    lines = f.readlines()


# Part 1

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum_ids = 0
for line in lines:
    l = line.strip()

    aux = l.split(":")

    game_id = int(aux[0].split()[1])
    cube_sets = aux[1].split(";")

    impossible_game = False
    for s in cube_sets:
        cubes = s.split(",")

        for cube in cubes:
            c = cube.split()

            if bag[c[1]] < int(c[0]):
                impossible_game = True
                break
        
        if impossible_game:
            break
    
    if not impossible_game:
        sum_ids += game_id

print(sum_ids)

# Part 2

sum_power = 0

for line in lines:
    l = line.strip()

    aux = l.split(":")
    cube_sets = aux[1].split(";")

    game_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for s in cube_sets:
        cubes = s.split(",")

        for cube in cubes:
            c = cube.split()

            game_cubes[c[1]] = max(game_cubes[c[1]], int(c[0]))
        
    
    game_power = 1
    for color in game_cubes:
        game_power *= game_cubes[color]
    
    
    sum_power += game_power

print(sum_power)