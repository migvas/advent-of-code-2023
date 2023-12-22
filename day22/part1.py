bricks = {}
set_bricks = {}
is_supported = {}
z_pos = []

def is_blocked(a,b):
    return (a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1]) or (a[0] < b[0] and a[1] > b[1])

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

id = 0
for l in data:
    brick_start, brick_end = l.strip().split("~")

    x_s, y_s, z_s = brick_start.split(",")
    x_e, y_e, z_e = brick_end.split(",")

    x = (int(x_s), int(x_e))
    y = (int(y_s), int(y_e))

    z = [int(z_s), int(z_e)]
    
    
    if z[0] not in bricks:
        bricks[z[0]] = []

    bricks[z[0]].append({
        "x": x,
        "y": y,
        "z": z,
        "id": id
    })

    id += 1

    if z[0] not in z_pos:
        z_pos.append(z[0])
        z_pos.sort()


for pos in z_pos:
    bricks_falling = bricks[pos]

    while bricks_falling:
        brick = bricks_falling.pop()

        x = brick["x"]
        y = brick["y"]
        z = brick["z"]
        id = brick["id"]

        is_supported[id] = []
        while z[0] > 1:
                next_z = z[0] - 1

                z_bricks = set_bricks.get(next_z)
                if z_bricks:
                    set_brick = False
                    for b in z_bricks:
                        x_support = is_blocked(x, b["x"])
                        y_support = is_blocked(y, b["y"])

                        if x_support and y_support:
                            is_supported[id].append(b["id"])
                            set_brick = True

                    if set_brick:
                        break

                    
                z[0] -= 1
                z[1] -= 1

        if z[1] not in set_bricks:
            set_bricks[z[1]] = []

        set_bricks[z[1]].append({
            "x": x,
            "y": y,
            "id": id
        })

cannot_remove = {}

for supports in is_supported.values():
    if len(supports) == 1:
        cannot_remove[supports[0]] = True

print(len(data) - len(cannot_remove.keys()))
