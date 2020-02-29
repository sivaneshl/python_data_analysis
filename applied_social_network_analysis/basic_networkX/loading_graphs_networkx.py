import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Instantiate the graph
G1 = nx.Graph()
# add node/edge pairs
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (0, 5),
                   (1, 3),
                   (1, 6),
                   (3, 4),
                   (4, 5),
                   (4, 7),
                   (5, 8),
                   (8, 9)])

# draw the graph G1
nx.draw_networkx(G1)
plt.show()

# loading a graph from an adjacency list
G2 = nx.read_adjlist('G_adjlist.txt', nodetype=int)
print(G2.edges())

# adjacency matrix
G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
G3 = nx.Graph(G_mat)
print(G3.edges())

# edgelist
# The edge list format represents edge pairings in the first two columns. Additional edge attributes
# can be added in subsequent columns. Looking at G_edgelist.txt this is the same as the original graph G1,
# but now each edge has a weight.
# For example, from the first row, we can see the edge between nodes 0 and 1, has a weight of 4.
G4 = nx.read_edgelist('G_edgelist.txt', data=[('Weight', int)], nodetype=int)
print(G4.edges(data=True))


# create a graph from a dataframe
G_df = pd.read_csv('G_edgelist.txt', delim_whitespace=True,
                   header=None, names=['n1', 'n2', 'weight'])
G5 = nx.from_pandas_edgelist(G_df, 'n1', 'n2', edge_attr='weight')
print(G5.edges(data=True))


