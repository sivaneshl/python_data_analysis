import networkx as nx
from networkx.algorithms import bipartite

B = nx.Graph()  # no separate class for bipartite
B.add_nodes_from(['A', 'B', 'C', 'D', 'E'], bipartite=0)    # label for one set of nodes 0
B.add_nodes_from([1, 2, 3, 4], bipartite=1)     # label for another set of nodes 1
B.add_edges_from([('A', 1), ('B', 1), ('C', 1), ('D', 2), ('E', 3), ('E', 4)])

# check if the graph is bipartite
print(bipartite.is_bipartite(B))
# add an edge from A to Bto make the graph  non bipartite and check again
B.add_edge('A', 'B')
print(bipartite.is_bipartite(B))
# remove the edge A-B and check again
B.remove_edge('A', 'B')
print(bipartite.is_bipartite(B))


# check if a set of nodes is a bipartition of the graph
X = set([1, 2, 3, 4])
print(bipartite.is_bipartite_node_set(B, X))
X = set([1, 2, 3, 4, 'A'])
print(bipartite.is_bipartite_node_set(B, X))


# get each set of nodes of the bipartite graph
print(bipartite.sets(B))
# add an edge from A to Bto make the graph  non bipartite and get the sets again
B.add_edge('A', 'B')
# print(bipartite.sets(B))    # error
B.remove_edge('A', 'B')




