import networkx as nx

# betweenness centrality = important nodes are the nodes that connect other nodes
# sum of the ratio of the shortest path between nodes s and t that contain node v and
# the number of shortest paths between nodes s and t for all possible nodes s and t

# exercise
G = nx.from_edgelist([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'),
                      ('D', 'E'), ('E', 'F'), ('E', 'G'), ('F', 'G')])
print(nx.betweenness_centrality(G, endpoints=False, normalized=False))

# normalization
# undirected graphs = 0.5*(N-1)*(N-2)
# directed graphs = (N-1)*(N-2)
print(nx.betweenness_centrality(G, endpoints=False, normalized=True))

# using karate club example
import operator
G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)
btwnCent = nx.betweenness_centrality(G, normalized=True, endpoints=False)
print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[0:5])

# approximation
# use only 10 nodes to compute the centrality
btwnCent_approx = nx.betweenness_centrality(G, normalized=True, endpoints=False, k=10)
print(sorted(btwnCent_approx.items(), key=operator.itemgetter(1), reverse=True)[0:5])


# define specific set of source nodes and target nodes - subsets
btwnCent_subsets = nx.betweenness_centrality_subset(G, [34, 33, 21, 30, 16, 27, 15, 23, 10],
                                                    [1, 4, 13, 11, 6, 12, 17, 7], normalized=True)
print(sorted(btwnCent_subsets.items(), key=operator.itemgetter(1), reverse=True)[0:5])


# betweenness centrality of an edge
# ratio of the number of shortest path between nodes s and t involving edge e
# and the total number of shortest path between nodes s and t
btwnCent_edge = nx.edge_betweenness_centrality(G, normalized=True)
print(sorted(btwnCent_edge.items(), key=operator.itemgetter(1), reverse=True)[0:5])

# define specific source and target nodes
btwnCent_edge_subset = nx.edge_betweenness_centrality_subset(G,
                                                             [34, 33, 21, 30, 16, 27, 15, 23, 10],
                                                             [1, 4, 13, 11, 6, 12, 17, 7],
                                                             normalized=True)
print(sorted(btwnCent_edge_subset.items(), key=operator.itemgetter(1), reverse=True)[0:5])





