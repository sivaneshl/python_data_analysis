import operator
import networkx as nx
import matplotlib.pyplot as plt

G = nx.from_edgelist([('A','B'), ('A','D'), ('A','E'), ('B','D'), ('B','C'), ('C','D'),
                      ('C','F'), ('E','F'), ('E','G'), ('F','G'), ('G','H'), ('G','I')])
nx.draw_networkx(G)
# plt.show()

# common neighbors
common_neigh = [(e[0], e[1], len(list(nx.common_neighbors(G, e[0], e[1])))) for e in nx.non_edges(G)]
print(sorted(common_neigh, key=operator.itemgetter(2), reverse=True))

# jaccard coefficient = nbr of common neighbors divided by nbr of total neighbors for nodes x & y
jaccard = list(nx.jaccard_coefficient(G))
print(sorted(jaccard, key=operator.itemgetter(2), reverse=True))

# resource allocation index
# sum of (1/degree of the node) that are the common neighbors of x and y
res_alloc = list(nx.resource_allocation_index(G))
print(sorted(res_alloc, key=operator.itemgetter(2), reverse=True))

# adamic-adar index
# sum of (1/log of degree of the node) that are the common neighbors of x and y
adamic_adar = list(nx.adamic_adar_index(G))
print(sorted(adamic_adar, key=operator.itemgetter(2), reverse=True))

# preferential attachment = product of the degree of the two nodes
pref_attach = list(nx.preferential_attachment(G))
print(sorted(pref_attach, key=operator.itemgetter(2), reverse=True))

# community common neighbors = common neighbor soundarajan-hopcroft score
# adds a bonus 1 if the nodes are in the same community
# group nodes by community
G.nodes['A']['community']=0
G.nodes['B']['community']=0
G.nodes['C']['community']=0
G.nodes['D']['community']=0
G.nodes['E']['community']=1
G.nodes['F']['community']=1
G.nodes['G']['community']=1
G.nodes['H']['community']=1
G.nodes['I']['community']=1
community_common_neigh = list(nx.cn_soundarajan_hopcroft(G))
print(sorted(community_common_neigh, key=operator.itemgetter(2), reverse=True))


# community resource allocation = resource alloaction soundarajan-hopcroft score
# adds a bonus 1 if the nodes are in the same community
community_res_alloc = list(nx.ra_index_soundarajan_hopcroft(G))
print(sorted(community_res_alloc, key=operator.itemgetter(2), reverse=True))
