import networkx as nx
import operator

G = nx.from_edgelist([('A', 'C'), ('A', 'E'), ('A', 'D'), ('B', 'D'), ('C', 'G'),
                      ('D', 'G'), ('D', 'H'), ('D', 'E'), ('E', 'H'), ('H', 'F')])

res_alloc = list(nx.resource_allocation_index(G))
print(sorted(res_alloc, key=operator.itemgetter(2), reverse=True))

pref_attach = list(nx.preferential_attachment(G))
print(sorted(pref_attach, key=operator.itemgetter(2), reverse=True))

G.node['A']['community']=0
G.node['B']['community']=0
G.node['C']['community']=0
G.node['D']['community']=0
G.node['G']['community']=0
G.node['F']['community']=1
G.node['E']['community']=1
G.node['H']['community']=1

community_common_neigh = list(nx.cn_soundarajan_hopcroft(G))
print(sorted(community_common_neigh, key=operator.itemgetter(2), reverse=True))
community_res_alloc = list(nx.ra_index_soundarajan_hopcroft(G))
print(sorted(community_res_alloc, key=operator.itemgetter(2), reverse=True))

