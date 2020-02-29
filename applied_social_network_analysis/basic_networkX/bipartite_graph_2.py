import networkx as nx
from networkx.algorithms import bipartite

# L-bipartite graph projection
B = nx.Graph()
B.add_edges_from([('A', 1), ('B', 1), ('C', 1), ('D', 1), ('H', 1),
                  ('B', 2), ('C', 2), ('D', 2), ('E', 2), ('G', 2),
                  ('E', 3), ('F', 3), ('H', 3), ('J', 3),
                  ('E', 4), ('I', 4), ('J', 4)])

X = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# projectd graph of left side nodes
p_L = bipartite.projected_graph(B, X)

Y = set([1, 2, 3, 4])
# projected graph of right side nodes
p_R = bipartite.projected_graph(B, Y)

# L-bipartite weighted graph projection
Y = set([1, 2, 3, 4])
# projected graph of right side nodes
p_R = bipartite.weighted_projected_graph(B, Y)
