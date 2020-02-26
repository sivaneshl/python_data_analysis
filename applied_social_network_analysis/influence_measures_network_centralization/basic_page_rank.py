import networkx as nx

G = nx.gnm_random_graph(5, 10, directed=True)
print(G.edges())

print(nx.pagerank(G))
# alpha damping probability -  scaled pagerank
print(nx.pagerank(G, alpha=0.8))