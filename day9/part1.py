data_file = "data.txt"

with open(data_file) as f:
    report = f.readlines()

value_sum = 0

for line in report:
    current = [int(c) for c in line.split()]

    last_vals = 0

    while 1:
        last_vals += current[-1]
        break_loop = True
        for val in current:
            if val:
                break_loop = False
                break

        if break_loop:
            break

        next_seq = [current[i] - current[i-1] for i in range(1, len(current))]

        current = next_seq

    value_sum += last_vals

print(value_sum)
