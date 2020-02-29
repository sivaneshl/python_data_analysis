import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'K'), ('F', 'G'),
                  ('C', 'E'), ('C', 'F'), ('D', 'E'), ('E', 'F'), ('E', 'H'), ('I', 'J')])
print(nx.clustering(G, 'F'))    # clustering coeff of node F
print(nx.clustering(G, 'A'))
print(nx.clustering(G, 'J'))

# clustering co-eff for the network as a whole
# approach 1 = average of clustering coeff of all nodes
print(nx.average_clustering(G))
# approach 2 - percentage of open traids (3 nodes connected by 2 edges) that are triangles in the network
# transitivity - ratio of number of triangles and number of open triads in a network
print(nx.transitivity(G))
