import networkx as nx

G = nx.gnm_random_graph(5, 10, directed=True)
print(G.edges())

# this function will return 2 dictionaries one for hubs and the other for authorities
# with the nodes as the key
print(nx.hits(G))
