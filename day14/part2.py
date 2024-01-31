from collections import deque

grid = []
directions = ["north", "west", "south", "east"]


def run_cycle(grid):
    m = grid

    for _ in range(4):
        i = 0

        while i < len(m):
            for j in range(len(m[i])):
                if m[i][j] == "O":
                    k = i
                    while k > 0 and m[k - 1][j] == '.':
                        m[k][j] = '.'
                        m[k - 1][j] = "O"
                        k -= 1
            i += 1


        m = rotate_right(m)
    
    return m


def rotate_right(mat):
    t = []

    for i in range(len(mat) - 1, -1, -1):
        for j in range(len(mat[i])):
            if len(t) < j + 1:
                t.append([])
            t[j].append(mat[i][j])

    return t

def compute_load(grid):
    load = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                load += len(grid) - i

    return load

def hash_mat(mat):
    t = ''
    for r in mat:
        t += "".join(r)
    
    return t

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()


for line in data:
    grid.append(list(line.strip()))


hashtable = {}
old_grid = grid
old_hash = hash_mat(grid)
loads = {}
cycles = 1
diff = 0
while 1:
    if not hashtable.get(old_hash):
        new_grid = run_cycle(old_grid)
        hashtable[old_hash] = {
            "grid": new_grid,
            "hash": hash_mat(new_grid),
            "id": cycles
        }
        loads[cycles] = compute_load(new_grid)
    else:
        print(hashtable[old_hash]["id"])
        diff = cycles - hashtable[old_hash]["id"]
        break
    new_grid_obj = hashtable[old_hash]
    old_grid = new_grid_obj["grid"]
    old_hash = new_grid_obj["hash"]
    cycles += 1

print(diff)
print(hashtable[old_hash]["id"] + (1000000000 - hashtable[old_hash]["id"]) % diff)
print(loads[hashtable[old_hash]["id"] + (1000000000 - hashtable[old_hash]["id"]) % diff])