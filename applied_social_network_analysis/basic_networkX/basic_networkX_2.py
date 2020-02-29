import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', relation='family', weight=6)
G.add_edge('B', 'C', relation='friend', weight=13)

print(G.edges())    # list all edges

print(G.edges(data=True))   # list edges with attributes

print(G.edges(data='relation'))     # list a particular attribute

print(G.edge['A']['B'])     # dict of attributes for egde(A,B)

print(G.edge['B']['C']['weight'])   # particular attribute for edge(A,B)

print(G.edge['C']['B']['weight'])   # undirected graph - does not mater

# directed graph
di_G = nx.DiGraph()
di_G.add_edge('A', 'B', relation='family', weight=6)
di_G.add_edge('B', 'C', relation='friend', weight=13)

print(di_G.edge['B']['C']['weight'])   # particular attribute for edge(A,B)
# print(di_G.edge['C']['B']['weight'])   # directed graph - error

# multigraph
G = nx.MultiGraph()
G.add_edge('A', 'B', relation='family', weight=6)
G.add_edge('A', 'B', relation='friend', weight=18)
G.add_edge('C', 'B', relation='friend', weight=13)

print(G.edge['A']['B']) # one dict of attrinutes per edge(A,B)

print(G.edge['A']['B'][0]['weight'])    # to get the first egde of A, B
print(G.edge['A']['B'][1]['weight'])    # to get the 2nd edge of A, B

# dircted multigraph
G = nx.MultiDiGraph()
G.add_edge('A', 'B', relation='family', weight=6)
G.add_edge('A', 'B', relation='friend', weight=18)
G.add_edge('C', 'B', relation='friend', weight=13)

print(G.edge['A']['B'][0]['weight'])    # to get the first egde of A, B
# print(G.edge['B']['A'][0]['weight'])    # directed - error

# node attributes
G = nx.Graph()
G.add_edge('A', 'B', relation='family', weight=6)
G.add_edge('B', 'C', relation='friend', weight=13)

G.add_node('A', role='trader')
G.add_node('B', role='trader')
G.add_node('C', role='manager')

print(G.nodes())    # list all nodes
print(G.nodes(data=True))   # list nodes with attributes
print(G.node['A']['role'])  # get a particular node and particular attribte