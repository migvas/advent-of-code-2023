data_file = "data.txt"

def convert_val(value, conversion_map):
    new_val = {
        "type": conversion_map["to"]
    }

    for m in conversion_map["map"]:
        if value >= m["start"] and value <= m["end"]:
            new_val["value"] = value + m["increment"]
            return new_val
        
    new_val["value"] = value
    return new_val 

current_values = []
map_list = {}
with open(data_file) as f:
    seed_line = f.readline().strip()
    seeds = seed_line.split(":")[1].split()
    for seed in seeds:
        current_values.append({
            "type": "seed",
            "value": int(seed)
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
    for i in range(len(current_values)):
        current_values[i] = convert_val(current_values[i]["value"], map_list[current_values[i]["type"]])
    if current_values[0]["type"] == "location":
        break


    
min_location = current_values[0]["value"]
for c in current_values:
    min_location = min(min_location, c["value"])

print(min_location)