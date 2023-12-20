import sys
data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

graph = []
for i in range(len(data)):
    line = data[i].strip()
    graph.append([])
    for j in range(len(line)):
        graph[i].append(int(data[i][j]))

visited = {}

cost_q = {}

def compute_neighbor(cost, x, y, dx, dy, steps):
    x += dx
    y += dy

    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
        return
    

    new_cost = cost + graph[x][y]

    if x == len(graph) - 1 and y == len(graph[0]) - 1 and steps >= 4:
        print(new_cost)
        sys.exit(0)

    if (x, y, dx, dy, steps) not in visited:
        if not new_cost in cost_q:
            cost_q[new_cost] = []

        cost_q[new_cost].append((x, y, dx, dy, steps))

        visited[(x, y, dx, dy, steps)] = True


compute_neighbor(0, 0, 0, 1, 0, 1)
compute_neighbor(0, 0, 0, 0, 1, 1)

while 1:

    min_cost = min(cost_q.keys())

    next_nodes = cost_q.pop(min_cost)

    for node in next_nodes:
        x, y, dx, dy, steps = node

        if steps >= 4:
            compute_neighbor(min_cost, x, y, -dy, dx, 1)
            compute_neighbor(min_cost, x, y, dy, -dx, 1)
        
        if steps < 10:
            compute_neighbor(min_cost, x, y, dx, dy, steps + 1)