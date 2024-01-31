data_file = "data.txt"

def compute_arrangements(sm, rec):
    if not len(sm):
        if not len(rec):
            return 1
        else:
            return 0
    
    total_arrangements = 0
    if len(rec):
        next_springs = "#" * int(rec[0])
        if len(next_springs) < len(sm):
            next_springs += "."
        elif len(next_springs) > len(sm):
            return 0
        can_fit = True
        for i in range(0, len(next_springs)):
            if sm[i] != "?" and sm[i] != next_springs[i]:
                can_fit = False
                break
        if can_fit:
            total_arrangements += compute_arrangements(sm[len(next_springs):], rec[1:])
    
    if sm[0] == "." or sm[0] == "?":
        total_arrangements += compute_arrangements(sm[1:], rec)

    return total_arrangements


with open(data_file) as f:
    data = f.readlines()

total_arrangements = 0
for d in data:
    line = d.strip().split()
    spring_map = line[0]
    spring_records = line[1].split(",")

    total_arrangements += compute_arrangements(spring_map, spring_records)

print(total_arrangements)