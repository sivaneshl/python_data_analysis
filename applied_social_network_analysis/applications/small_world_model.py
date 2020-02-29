import networkx as nx
import matplotlib.pyplot as plt

G = nx.watts_strogatz_graph(1000, 6, 0.04)
degrees = dict(G.degree())
print(degrees)
degree_values = sorted(set(degrees.values()))
print(degree_values)
plot_values = [list(degrees.values()).count(i) / len(G.nodes()) for i in degree_values]
print(plot_values)

plt.bar(degree_values, plot_values)
plt.xlabel('Degree')
plt.ylabel('Fraction of nodes')
plt.show()


