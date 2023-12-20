from collections import deque

directions = {
    (0,1): {
        "l": (-1, 0),
        "r": (1,0)
    },
    (0,-1): {
        "l": (1, 0),
        "r": (-1,0)
    },
    (1,0): {
        "l": (0, 1),
        "r": (0, -1)
    },
    (-1, 0): {
        "l": (0, -1),
        "r": (0, 1)
    }
}


def comp_heat_loss(pos, direction, steps, visited):
    if pos[0] == len(data) - 1 and pos[1] == len(data[0]) - 2:
        return int(data[pos[0]][pos[1]])

    if pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0]) - 1 or pos in visited:
        return 10000000

    visited.append(pos)

    # go left
    l_direction = directions[direction]["l"]
    l_loss = comp_heat_loss(
        (pos[0] + l_direction[0], pos[1] + l_direction[1]), l_direction, 1, visited.copy())

    # go right
    r_direction = directions[direction]["r"]
    r_loss = comp_heat_loss(
        (pos[0] + r_direction[0], pos[1] + r_direction[1]), r_direction, 1, visited.copy())

    # go staright
    s_loss = 10000000
    if steps <= 3:
        s_loss = comp_heat_loss(
            (pos[0] + direction[0], pos[1] + direction[1]), direction, steps + 1, visited.copy())

    return min(l_loss, r_loss, s_loss) + int(data[pos[0]][pos[1]])


data_file = "test.txt"

with open(data_file) as f:
    data = f.readlines()

graph = []
distances = []
for i in range(len(data)):
    line = data[i].strip()
    graph.append([])
    distances.append([])
    for j in range(len(line)):
        graph[i].append(int(data[i][j]))
        costs = {}
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            costs[d] = {
                "cost": 10000000000,
                "steps": 0
            }
        distances[i].append(costs)

distances[0][0][(0,1)]["cost"] = 0
visited = {}
number_visited = 0
while 1:
    if number_visited == len(graph) * (len(graph[0])) * 4:
        break

    min_dist = 1000000000
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            for di in distances[i][j]:
                if distances[i][j][di]["cost"] < min_dist:
                    if not visited.get((i,j)):
                        min_dist = distances[i][j][di]["cost"]
                        next_node = (i, j)
                        node_details = distances[i][j][di]
                        next_node_direction = di
                    elif not visited[(i,j)].get(di):
                        min_dist = distances[i][j][di]["cost"]
                        next_node = (i, j)
                        node_details = distances[i][j][di]
                        next_node_direction = di

    if not visited.get(next_node):
        visited[next_node] = {
            next_node_direction: True
            }
    else:
        visited[next_node][next_node_direction] = True
    number_visited += 1

    for direction in directions[next_node_direction]:
        d = directions[next_node_direction][direction]
        adjacent = (next_node[0] + d[0], next_node[1] + d[1])
        if adjacent[0] < 0 or adjacent[0] >= len(data) or adjacent[1] < 0 or adjacent[1] >= len(data[0]) - 1:
            continue

        if distances[adjacent[0]][adjacent[1]][d]["cost"] >= distances[next_node[0]][next_node[1]][next_node_direction]["cost"] + graph[adjacent[0]][adjacent[1]]:
            distances[adjacent[0]][adjacent[1]][d]["cost"] = distances[next_node[0]
                                                                    ][next_node[1]][next_node_direction]["cost"] + graph[adjacent[0]][adjacent[1]]
            distances[adjacent[0]][adjacent[1]][d]["steps"] = 1

    if node_details["steps"] < 3:
        adjacent = (next_node[0] + next_node_direction[0], next_node[1] + next_node_direction[1])
        if adjacent[0] < 0 or adjacent[0] >= len(data) or adjacent[1] < 0 or adjacent[1] >= len(data[0]) - 1:
            continue

        if distances[adjacent[0]][adjacent[1]][next_node_direction]["cost"] > distances[next_node[0]][next_node[1]][next_node_direction]["cost"] + graph[adjacent[0]][adjacent[1]]:
            distances[adjacent[0]][adjacent[1]][next_node_direction]["cost"] = distances[next_node[0]
                                                                    ][next_node[1]][next_node_direction]["cost"] + graph[adjacent[0]][adjacent[1]]

            distances[adjacent[0]][adjacent[1]][next_node_direction]["steps"] = node_details["steps"] + 1
        elif distances[adjacent[0]][adjacent[1]][next_node_direction]["cost"] == distances[next_node[0]][next_node[1]][next_node_direction]["cost"] + graph[adjacent[0]][adjacent[1]] and distances[adjacent[0]][adjacent[1]][next_node_direction]["steps"] > node_details["steps"] + 1:
            distances[adjacent[0]][adjacent[1]][next_node_direction]["cost"] = distances[next_node[0]
                                                                    ][next_node[1]][next_node_direction]["cost"] + graph[adjacent[0]][adjacent[1]]

            distances[adjacent[0]][adjacent[1]][next_node_direction]["steps"] = node_details["steps"] + 1

print(distances[0][6])
