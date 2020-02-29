import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gpickle('resources/major_us_cities')

fig = plt.figure(figsize=(10, 9))
nx.draw_networkx(G)     # uses default spring layout

# using random layout
plt.figure(figsize=(10, 9))
pos = nx.random_layout(G)
nx.draw_networkx(G, pos)

# circular layour
plt.figure(figsize=(10, 9))
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos)

# using own layout by passing positions as the 'location' attribute
plt.figure(figsize=(10, 9))
pos = nx.get_node_attributes(G, 'location')
nx.draw_networkx(G, pos)

# change attributes
plt.figure(figsize=(10, 9))
nx.draw_networkx(G, pos, alpha=0.7,     # transparency
                 with_labels=False,     # remove labels
                 edge_color='0.4')      # make edges grey
plt.axis('off')     # remove the axis
plt.tight_layout()  # reduce padding

# change node color, size and edge width
plt.figure(figsize=(10, 7))
node_color = [G.degree(v) for v in G]   # set the node color based on the degree of the node
node_size = [0.0005*nx.get_node_attributes(G, 'population')[v] for v in G]  # set the node size based on the population attribute
edge_width = [0.0005*G[u][v]['weight'] for u, v in G.edges()]   # set the edge width based on weight of the edge
nx.draw_networkx(G, pos, node_size=node_size, node_color=node_color, edge_width=edge_width,
                 alpha=0.7, with_labels=False, edge_color='0.4', cmap=plt.cm.Blues)
plt.axis('off')     # remove the axis
plt.tight_layout()  # reduce padding

# draw specific edges and add labels to specific nodes
greater_than_770 = [x for x in G.edges(data=True) if x[2]['weight'] > 770]
nx.draw_networkx_edges(G, pos, edgelist=greater_than_770, edge_color='r', alpha=0.7, edge_width=6)
nx.draw_networkx_labels(G, pos, labels={'Los Angeles, CA': 'LA', 'New York, NY': 'NYC'},
                        font_size=18, font_color='white')
plt.axis('off')     # remove the axis
plt.tight_layout()  # reduce padding





plt.show()