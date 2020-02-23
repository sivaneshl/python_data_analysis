import networkx as nx
from networkx.algorithms import bipartite

# Use NetworkX to construct the bipartite weighted graph projection of nodes A,B,C,D,E,F
# and find the weight of the edge (A,C).
# What is the weight of the edge (A,C)?

B = nx.Graph()
B.add_edges_from([('A', 'G'),('A','I'), ('B','H'), ('C', 'G'), ('C', 'I'),('D', 'H'), ('E', 'I'), ('F', 'G'), ('F', 'J')])
X1 = set(['A', 'B', 'C', 'D', 'E', 'F'])

print(bipartite.sets(B))

p = bipartite.weighted_projected_graph(B, X1)
print(p.edge['A']['C'])

print(p)
