data_file = "data.txt"

with open(data_file) as f:
    data = f.readline().strip().split(",")


total = 0

for step in data:
    current_val = 0
    for c in step:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    
    total += current_val

print(total)