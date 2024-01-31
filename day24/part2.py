from sympy import symbols, solve

data_file = "data.txt"

rpx = symbols("rpx")
rpy = symbols("rpy")
rpz = symbols("rpz")
rvx = symbols("rvx")
rvy = symbols("rvy")
rvz = symbols("rvz")
t1 = symbols("t1")
t2 = symbols("t2")
t3 = symbols("t3")

with open(data_file) as f:
    data = f.readlines()

equations = []
times = [t1, t2, t3]

for i in range(0, 3):
    p, v = data[i].strip().split(" @ ")

    px, py, pz = p.split(", ")
    vx, vy, vz = v.split(", ")

    equations.append(rpx + times[i] * rvx - int(px) - times[i] * int(vx))
    equations.append(rpy + times[i] * rvy - int(py) - times[i] * int(vy))
    equations.append(rpz + times[i] * rvz - int(pz) - times[i] * int(vz))

sol = solve(equations)
print(sol[0][rpx] + sol[0][rpy] + sol[0][rpz])


