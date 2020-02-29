import networkx as nx
import matplotlib.pyplot as plt

G = nx.barabasi_albert_graph(100000, 1) # a graph with 100000 nodes where each new node attaches to
#  one existing node based on the preferential attachment
degrees = dict(G.degree())
print(degrees)
degree_values = sorted(set(degrees.values()))
print(degree_values)
plot_values = [list(degrees.values()).count(i) / len(G.nodes()) for i in degree_values]
print(plot_values)

plt.plot(degree_values, plot_values, 'o')
plt.xlabel('Degree')
plt.ylabel('Fraction of nodes')
plt.xscale('log')
plt.yscale('log')
plt.show()


