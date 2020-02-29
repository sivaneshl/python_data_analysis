import networkx as nx

G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)

print(nx.average_shortest_path_length(G))
print(nx.diameter(G))
print(nx.radius(G))
print(nx.center(G))
print(nx.periphery(G))
