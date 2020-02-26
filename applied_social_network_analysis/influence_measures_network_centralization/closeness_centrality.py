import networkx as nx

# closeness centrality = important nodes are close to other nodes
# closeness centrality = (number of nodes - 1) / sum of the length of shortest path from u to v
G = nx.karate_club_graph()
closeCent = nx.closeness_centrality(G)
print(closeCent[32])

# derivation
print ((len(G.nodes()) - 1) / sum(nx.shortest_path_length(G, 32).values()))

# disconnected nodes
# normalize by the number of nodes that the given node can reach
closeCent = nx.closeness_centrality(G, normalized=True)
print(closeCent[32])


# exercise
G = nx.from_edgelist([('A', 'B'), ('B', 'C'), ('C', 'D')], create_using=nx.DiGraph())
closeCent = nx.closeness_centrality(G, normalized=True)
print([closeCent[node] for node in G.nodes()])