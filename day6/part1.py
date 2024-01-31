data_file = "data.txt"

with open(data_file, "r") as f:
    time_line = f.readline()
    distance_line = f.readline()

times = time_line.split(":")[1].strip().split()
distances = distance_line.split(":")[1].strip().split()

margin = 1
for idx, time in enumerate(times):
    hold_time = 0
    race_time = int(time)
    record_distance = int(distances[idx])
    while hold_time <= race_time:
        distance = (race_time - hold_time) * hold_time
        if distance > record_distance:
            break
        hold_time += 1

    margin *= race_time - 2 * hold_time + 1

print(margin)
