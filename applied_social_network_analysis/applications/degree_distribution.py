import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnm_random_graph(10, 20)
degrees = dict(G.degree())
print(degrees)
degree_values = sorted(set(degrees.values()))
print(degree_values)
histogram = [list(degrees.values()).count(i) / len(G.nodes()) for i in degree_values]
print(histogram)

plt.bar(degree_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of nodes')
plt.show()


