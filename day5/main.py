data_file = "data.txt"

def convert_val(start, end, conversion_map):
    new_vals = []
    for m in conversion_map["map"]:
        if start >= m["start"] and end <= m["end"]:
            new_vals.append({
            "type": conversion_map["to"],
            "start": start + m["increment"],
            "end": end + m["increment"]
        })
            return new_vals
        elif start >= m["start"] and start <= m["end"]:
            new_vals.append({
            "type": conversion_map["to"],
            "start": start + m["increment"],
            "end": m["end"] + m["increment"]
        })
            start = m["end"] + 1
        elif end >= m["start"] and end <= m["end"]:
            new_vals.append({
            "type": conversion_map["to"],
            "start": m["start"] + m["increment"],
            "end": end + m["increment"]
        })
            end = m["start"] - 1
        elif start < m["start"] and end > m["end"]:
            new_vals.extend(convert_val(start, m["start"] - 1, conversion_map))
            new_vals.append({
            "type": conversion_map["to"],
            "start": m["start"] + m["increment"],
            "end": m["end"] + m["increment"]
            })
            new_vals.extend(convert_val(m["end"] - 1, end, conversion_map))
            return new_vals
            
        
    if not new_vals or start < end:
        new_vals.append({
            "type": conversion_map["to"],
            "start": start,
            "end": end
        })

    return new_vals

current_values = []
map_list = {}
with open(data_file) as f:
    seed_line = f.readline().strip()
    seeds = seed_line.split(":")[1].split()
    for i in range(0,len(seeds), 2):
        current_values.append({
            "type": "seed",
            "start": int(seeds[i]),
            "end": int(seeds[i]) + int(seeds[i + 1]) - 1,
        })
    f.readline()
    while 1:
        next_line = f.readline()
        if not next_line:
            break

        instruction_set = next_line.strip().split("-to-")
        map_list[instruction_set[0]] = {
            "to": instruction_set[1].split()[0],
            "map":[]
        }

        while 1:
            map_line = f.readline().strip()
            if not map_line:
                break
            
            map_arr = map_line.split()
            new_map = {
                "start": int(map_arr[1]),
                "end": int(map_arr[1]) + int(map_arr[2]) - 1,
                "increment": int(map_arr[0]) - int(map_arr[1])
            }

            map_list[instruction_set[0]]["map"].append(new_map)

while 1:
    new_arr =[]
    for i in range(len(current_values)):
        new_arr.extend(convert_val(current_values[i]["start"], current_values[i]["end"], map_list[current_values[i]["type"]]))
    
    current_values = new_arr
    if current_values[0]["type"] == "location":
        break


    
min_location = current_values[0]["start"]
for c in current_values:
    min_location = min(min_location, c["start"])

print(min_location)