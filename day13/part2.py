data_file = "data.txt"

def transpose(mat):
    t = []

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if len(t) < j + 1:
                t.append([])
            t[j].append(mat[i][j])

    return t

def has_mirror(mat, row):
    i = row - 1
    j = row
    smudges = 0
    while i >= 0 and j < len(mat):
        for k in range(len(mat[0])):
            if mat[i][k] != mat[j][k]:
                smudges += 1
        if smudges > 1:
            return False
        i -= 1
        j += 1
        
    return smudges == 1

patterns = [[]]
idx = 0

with open(data_file) as f:
    while 1:
        line = f.readline()

        if not line:
            break

        clean_line = line.strip()

        if not clean_line:
            patterns.append([])
            idx += 1
            continue

        patterns[idx].append(clean_line)

horizontal = 0
vertical = 0
for pattern in patterns:
    has_horizontal = False
    for i in range(1, len(pattern)):
        if has_mirror(pattern, i):
            horizontal += i
            has_horizontal = True
            break
    
    if has_horizontal:
        continue

    transposed_mat = transpose(pattern)

    for i in range(1, len(transposed_mat)):
        if has_mirror(transposed_mat, i):
            vertical += i
            break


print(horizontal * 100 +  vertical)
