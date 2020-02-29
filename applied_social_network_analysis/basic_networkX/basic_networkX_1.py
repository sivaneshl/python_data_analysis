import networkx as nx

# undirected graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')

# directed graph
di_G = nx.DiGraph()
di_G.add_edge('B', 'A')
di_G.add_edge('B', 'C')

# weighted graphs
weight_G = nx.Graph()
weight_G.add_edge('A', 'B', weight=6)
weight_G.add_edge('B', 'C', weight=13)

# signed graphs
sign_G = nx.Graph()
sign_G.add_edge('A', 'B', sign='+')
sign_G.add_edge('B', 'C', sign='-')

# egde attributes
G = nx.Graph()
G.add_edge('A', 'B', relation='friend')
G.add_edge('B', 'C', relation='coworker')
G.add_edge('D', 'E', relation='family')

# multigraphs
multi_G = nx.Graph()
multi_G.add_edge('A', 'B', relation='friend')
multi_G.add_edge('A', 'B', relation='neighbor')
multi_G.add_edge('G', 'F', relation='coworker')
multi_G.add_edge('G', 'F', relation='friend')


