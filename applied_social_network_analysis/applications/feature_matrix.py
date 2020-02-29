import pandas as pd
import networkx as nx

G = nx.read_gpickle('../network_connectivity/resources/major_us_cities')
# print(G.nodes(data=True))

# Initialize the dataframe, using the nodes as the index
df = pd.DataFrame(index=G.nodes())

# Extracting attributes
# Using nx.get_node_attributes it's easy to extract the node attributes in the graph into DataFrame columns.
df['location'] = pd.Series(nx.get_node_attributes(G, 'location'))
df['population'] = pd.Series(nx.get_node_attributes(G, 'population'))


# Creating node based features
# Most of the networkx functions related to nodes return a dictionary, which can also easily be added to our dataframe.
df['clustering'] = pd.Series(nx.clustering(G))
df['degree'] = pd.Series(G.degree())
print(df.head())


# Edge based features
print(G.edges(data=True))

# Initialize the dataframe, using the edges as the index
df = pd.DataFrame(index=G.edges())

# Extracting attributes
# Using nx.get_edge_attributes, it's easy to extract the edge attributes in the graph into DataFrame columns.
df['weight'] = pd.Series(nx.get_edge_attributes(G, 'weight'))
# print(df.head())


# Creating edge based features
# Many of the networkx functions related to edges return a nested data structures. We can extract the relevant data using list comprehension.
df['pref_attach'] = [i[2] for i in nx.preferential_attachment(G, df.index)]

# In the case where the function expects two nodes to be passed in, we can map the index to a lamda function.
df['common_neigh'] = df.index.map(lambda e: len(list(nx.common_neighbors(G, e[0], e[1]))))

print(df.head())