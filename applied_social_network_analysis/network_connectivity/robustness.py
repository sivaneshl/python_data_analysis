import networkx as nx

G = nx.Graph()

# robustness - the ability of a network to maintain its genaral structure properties when it faces failures or attacks

# what is the smallest number of nodes that need to be removed to make it disconnected
nx.node_connectivity(G)
# which node
nx.minimum_node_cut(G)

# what is the smallest number of edges that need to be removed to make it disconnected
nx.edge_connectivity(G)
# which nodes
nx.minimum_edge_cut(G)

# robust networks are those that have a large edge cuts and node cuts

# simple paths
nx.all_simple_paths(G, 'G', 'L')    # all simple paths from node G to node L

# node connectivity
# how many nodes to be removed to block the connectivity of nodes G and L
nx.node_connectivity(G, 'G', 'L')
nx.minimum_node_cut(G, 'G', 'L')

# egde connectivity
# how many edges need to be removed to block the connectivity from G to L
nx.edge_connectivity(G, 'G', 'L')
nx.minimum_edge_cut(G, 'G', 'L')

