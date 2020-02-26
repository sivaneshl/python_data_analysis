import networkx as nx

G = nx.from_edgelist([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E'),
                      ('D', 'G'), ('E', 'G'), ('G', 'F')])

degCent = nx.degree_centrality(G)
print(degCent['D'])
# print(nx.degree(G, 'D')/(len(G.nodes())-1))

closeCent = nx.closeness_centrality(G)
print(closeCent['G'])

btwnCent = nx.betweenness_centrality(G, normalized=True, endpoints=False)
print(btwnCent['G'])

btwnCent_edge = nx.edge_betweenness_centrality(G, normalized=False)
print(btwnCent_edge[('G', 'F')])


G = nx.from_edgelist([('A', 'B'), ('B', 'A'), ('A', 'C'), ('C', 'D'), ('D', 'C')],
                     create_using=nx.DiGraph())
for alpha in [0.9, 0.95, 0.8, 0.5]:
    print(nx.pagerank(G, alpha=alpha))


G = nx.from_edgelist([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A'), ('D', 'C')],
                     create_using=nx.DiGraph())
print(nx.pagerank(G))
print(nx.hits(G))