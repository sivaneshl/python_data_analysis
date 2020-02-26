import networkx as nx

# measure of centrality = number of neighbors = degree
# undirected = degree of a node / (number of nodes - 1)
G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)
degCent = nx.degree_centrality(G)
print(degCent[34])  # degree centrality of node 34
print(degCent[33])  # degree centrality of node 33


# directed graph
# in-degree centrality = in-degree of a node / (number of nodes - 1)
nx.in_degree_centrality(G)
# out-degree centrality = out-degree of a node / (number of nodes - 1)
nx.out_degree_centrality(G)
