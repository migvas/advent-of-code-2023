import sys

sys.setrecursionlimit(10000)
directions = [(0,1), (1,0), (0, -1), (-1, 0)]
visited_nodes = {}
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = []

    def add_edge(self, parent_node, node, steps):
        if parent_node not in self.nodes:
            self.add_node(parent_node)
        if node not in self.nodes:
            self.add_node(node)
        

        self.nodes[parent_node].append({
            "node": node,
            "steps": steps
        })

        self.nodes[node].append({
            "node": parent_node,
            "steps": steps
        })

def build_graph(x, y, steps, parent_node):
    global visited_nodes
    
    if (x,y) == starting_pos:
        parent_node = (x, y)

    visited_nodes[(x,y)] = True
    if (x,y) == finish:
        G.add_edge(parent_node, (x,y), steps)
        return
    
    next_pos = []

    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if grid[new_x][new_y] != "#" and (new_x, new_y) not in visited_nodes:
                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                    next_pos.append((new_x, new_y))
        elif (new_x, new_y) in G.nodes and (new_x, new_y) != parent_node:
            G.add_edge(parent_node, (new_x, new_y), steps + 1)

    if len(next_pos) > 1:
        G.add_edge(parent_node, (x,y), steps)
        parent_node = (x,y)
        steps = 0
    
    for p in next_pos:
        build_graph(p[0], p[1], steps + 1, parent_node)
    
    return
    

def dfs(x, y, steps, visited):

    visited.append((x,y))
    if (x,y) == finish:
        return steps
    
    
    max_steps = 0
    for node in G.nodes[(x,y)]:
        d = node["node"]
        if d not in visited:
                dir_steps = dfs(d[0], d[1], steps + node["steps"], list(visited))
                if dir_steps > max_steps:
                    max_steps = dir_steps
    return max_steps

data_file = "data.txt"

with open(data_file) as f:
    data = f.readlines()

grid = []
for i, line in enumerate(data):
    grid.append([])
    for j, c in enumerate(line.strip()):
        grid[i].append(c)

        if c == ".":
            if i == 0:
                starting_pos = (i, j)
            if i == len(data) - 1:
                finish = (i, j)

G = Graph()

build_graph(starting_pos[0], starting_pos[1], 0, None)
print("Graph done")
print(dfs(starting_pos[0], starting_pos[1], 0, []))