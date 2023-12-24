from sympy import symbols, solve

data_file = "data.txt"

x = symbols("x")

with open(data_file) as f:
    data = f.readlines()

hailstones = []

for l in data:
    p, v = l.strip().split(" @ ")

    px, py, pz = p.split(", ")
    vx, vy, vz = v.split(", ")

    hailstones.append({"y": int(py) + int(vy)*((x-int(px))/int(vx)), "t": (x-int(px))/int(vx)})


crosses = 0

for i in range(len(hailstones) - 1):
    for j in range(i + 1, len(hailstones)):
        print(i, j)
        sol = solve(hailstones[i]["y"] - hailstones[j]["y"])
        if len(sol):
            x_cross = sol[0]
            y_cross = hailstones[i]["y"].subs({x:x_cross})
            t1_cross = hailstones[i]["t"].subs({x:x_cross})
            t2_cross = hailstones[j]["t"].subs({x:x_cross})
            if x_cross >= 200000000000000 and x_cross <= 400000000000000 and y_cross >= 200000000000000 and y_cross <= 400000000000000 and t1_cross > 0 and t2_cross > 0:
                crosses += 1

print(crosses)