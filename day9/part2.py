data_file = "data.txt"

with open(data_file) as f:
    report = f.readlines()

value_sum = 0

for line in report:
    current = [int(c) for c in line.split()]

    first_vals = []

    while 1:
        first_vals.append(current[0])
        break_loop = True
        for val in current:
            if val:
                break_loop = False
                break

        if break_loop:
            break

        next_seq = [current[i] - current[i-1] for i in range(1, len(current))]

        current = next_seq

    current_diff = first_vals[-1]
    for idx in range(len(first_vals) - 2, -1, -1):
        current_diff = first_vals[idx] - current_diff

    value_sum += current_diff

print(value_sum)
