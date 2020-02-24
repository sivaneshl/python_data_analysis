import networkx as nx

G = nx.Graph()

# an undirected graph is connected, if for every pair of nodes there is a path between them
nx.is_connected(G)

# connected component
# every node in the subset has a path to every other node
# no other node has a path to any of the nodes in the subset
nx.connected_components(G)

# find which connected component the given node belongs to
nx.node_connected_component(G, 'M')


# connectivity in directed graphs
# strongly connected - a directed path from u to v and a directed path from v to u exists
nx.is_strongly_connected(G)
# weekly connected - replace all directed edges to undeirected edges and check for connecivity
nx.is_weakly_connected(G)


# strongly connected components
# every node in the subset has a directed path to every other node
# no other node has a directed path to any of the nodes in the subset
nx.strongly_connected_components(G)

# weekly connected components
# replace all directed edges undirected
# check for connected components
nx.weakly_connected_components(G)
