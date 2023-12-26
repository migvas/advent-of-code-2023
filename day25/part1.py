import networkx as nx

data_file = "data.txt"

G=nx.Graph()

with open(data_file) as f:
    data = f.readlines()

for line in data:
    c1, c2 = line.strip().split(": ")

    if c1 not in G:
        G.add_node(c1)

    for node in c2.split(" "):
        if node not in G:
            G.add_node(node)
        
        G.add_edge(c1, node)

communities_generator = nx.community.girvan_newman(G)
top_level_communities = next(communities_generator)
print(len(top_level_communities))
print(len(top_level_communities[0])*len(top_level_communities[1]))