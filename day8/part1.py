from collections import deque
data_file = "data.txt"

nodes = {}

with open(data_file) as f:
    instructions = f.readline().strip()

    f.readline()

    while 1:
        node_map = f.readline().strip()

        if not node_map:
            break

        node_arr = node_map.split(" = ")

        node_paths = node_arr[1].split(", ")

        nodes[node_arr[0]] = {
            "L": node_paths[0][1:],
            "R": node_paths[1][:-1]
        }

steps_per_instruction = len(instructions)
total_steps = 0
q = deque(["AAA"])
current_instruction = instructions

while 1:
    current_node = q.popleft()

    if current_instruction == instructions and nodes[current_node].get("direct"):
        q.append(nodes[current_node]["direct"])
        total_steps += steps_per_instruction
    
    else:
        new_node = nodes[current_node][current_instruction[0]]
        total_steps += 1
        if new_node == "ZZZ":
            break

        q.append(new_node)
        if len(current_instruction) > 1:
            current_instruction = current_instruction[1:]
        else:
            current_instruction = instructions


print(total_steps)