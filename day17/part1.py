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

cost_q[(0, 0, 0, 1, 0)] = 0
cost_q[(0, 0, 1, 0, 0)] = 0

while 1:
    min_dist = 1000000000

    for n, d in cost_q.items():
        if d < min_dist and n not in visited:
            min_dist = d
            x, y, dx, dy, steps = n
            current_cost = d
    
    del cost_q[(x, y, dx, dy, steps)]
    if x == len(graph) - 1 and y == len(graph[0]) - 1:
        print(current_cost)
        break
    
    visited[(x, y, dx, dy, steps)] = True
    neighbors = [(x - dy, y + dx, -dy, dx, 1), (x + dy, y - dx, dy, -dx, 1)]

    for n in neighbors:
        if n[0] < 0 or n[0] >= len(graph) or n[1] < 0 or n[1] >= len(graph[0]):
            continue
        n_dist = 100000000
        if cost_q.get(n):
            n_dist = cost_q[n]
        if n_dist > current_cost + graph[n[0]][n[1]] and n not in visited:
            cost_q[n] = current_cost + graph[n[0]][n[1]]

    if steps < 3:
        n = (x + dx, y + dy, dx, dy, steps + 1)

        if n[0] < 0 or n[0] >= len(graph) or n[1] < 0 or n[1] >= len(graph[0]):
            continue
        n_dist = 100000000
        if cost_q.get(n):
            n_dist = cost_q[n]
        if n_dist > current_cost + graph[n[0]][n[1]] and n not in visited:
            cost_q[n] = current_cost + graph[n[0]][n[1]]