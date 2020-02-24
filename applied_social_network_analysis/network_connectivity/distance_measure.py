import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('B', 'C'), ('B', 'K'), ('F', 'G'), ('E', 'I'),
                  ('C', 'E'), ('C', 'F'), ('D', 'E'), ('E', 'F'), ('E', 'H'), ('I', 'J')])

# distance from one node to another node
print(nx.shortest_path(G, 'A', 'H'))
print(nx.shortest_path_length(G, 'A', 'H'))

# find the distance from one node to all other nodes
# breadth-first search
T = nx.bfs_tree(G, 'A')     # bfs from node A
print(T.edges())
# using shortest path
print(nx.shortest_path_length(G, 'A'))

# average shortest path length
print(nx.average_shortest_path_length(G))

# diameter - maximum distance between any pair of nodes
print(nx.diameter(G))

# eccentricity - largest distance between n and all other nodes
print(nx.eccentricity(G))

# raduis - minimum eccentricity of a graph
print(nx.radius(G))

# periphery - set of nodes that have eccentricity equal to the diameter
print(nx.periphery(G))

# center - set of nodes that have eccentricity equal to the radius
print(nx.center(G))