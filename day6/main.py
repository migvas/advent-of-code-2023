import math
data_file = "data.txt"

# Part 2
with open(data_file, "r") as f:
    time_line = f.readline()
    distance_line = f.readline()

times = time_line.split(":")[1].strip().split()
distances = distance_line.split(":")[1].strip().split()

time = "".join(times)
distance = "".join(distances)

margin = 1

hold_time = 0
race_time = int(time)
record_distance = int(distance)

# First try
# while hold_time <= race_time:
#     distance = (race_time - hold_time) * hold_time
#     if distance > record_distance:
#         break
#     hold_time += 1

# We can also see what is the minimum hold_time to get the record distance
# hold_time^2 - race_time*hold_time + record_distance = 0
# Using the quadratic formula

a = 1
b = -race_time
c = record_distance

min_hold_time = (-b - math.sqrt(b ** 2 - 4*a*c))/ (2*a)

if min_hold_time == math.ceil(min_hold_time):
    # if there's an int hold_time to reach the distance
    # the minimum hold time to beat the record should be that + 1
    min_hold_time += 1

margin *= race_time - 2 * math.ceil(min_hold_time) + 1

print(margin)
