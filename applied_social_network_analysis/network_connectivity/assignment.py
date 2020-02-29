import networkx as nx

# Assignment 2 - Network Connectivity
# In this assignment you will go through the process of importing and analyzing an internal email communication
# network between employees of a mid-sized manufacturing company. Each node represents an employee and each
# directed edge between two nodes represents an individual email. The left node represents the sender and the
# right node represents the recipient.

# Question 1
# Using networkx, load up the directed multigraph from email_network.txt.
# Make sure the node names are strings.
# This function should return a directed multigraph networkx graph.
def answer_one():
    G = nx.read_edgelist('resources/email_network.txt',
                         delimiter='\t',
                         data=[('time', int)],
                         create_using=nx.MultiDiGraph())
    return G

# Question 2
# How many employees and emails are represented in the graph from Question 1?
# This function should return a tuple (#employees, #emails).
def answer_two():
    G = answer_one()
    return (len(G.nodes()), len(G.edges()))

# Question 3
# Part 1. Assume that information in this company can only be exchanged through email.
# When an employee sends an email to another employee, a communication channel has been created,
# allowing the sender to provide information to the receiver, but not vice versa.#
# Based on the emails sent in the data, is it possible for information to go from every employee
# to every other employee?
# Part 2. Now assume that a communication channel established by an email allows information to be
# exchanged both ways.#
# Based on the emails sent in the data, is it possible for information to go from every employee
# to every other employee?
# This function should return a tuple of bools (part1, part2).
def answer_three():
    G = answer_one()
    return (nx.is_strongly_connected(G), nx.is_connected(G.to_undirected()))

# Question 4
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# This function should return an int.
def answer_four():
    G = answer_one()
    G_week = nx.weakly_connected_components(G)
    return len(max(G_week, key=len))

# Question 5
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# This function should return an int
def answer_five():
    G = answer_one()
    G_strong = nx.strongly_connected_components(G)
    return len(max(G_strong, key=len))

# Question 6
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of
# nodes in a largest strongly connected component. Call this graph G_sc.
# This function should return a networkx MultiDiGraph named G_sc.
def answer_six():
    G = answer_one()
    subgraphs = nx.strongly_connected_component_subgraphs(G)
    G_sc = max(subgraphs, key=len)
    return G_sc

G = answer_six()

# Question 7
# What is the average distance between nodes in G_sc?
# This function should return a float.
def answer_seven():
    return nx.average_shortest_path_length(G)


# Question 8
# What is the largest possible distance between two employees in G_sc?
# This function should return an int.
def answer_eight():
    return nx.diameter(G)


# Question 9
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# This function should return a set of the node(s).
def answer_nine():
    return nx.periphery(G)

# Question 10
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# This function should return a set of the node(s).
def answer_ten():
    return set(nx.center(G))


# Question 11
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal
# to the diameter of G_sc?
# How many nodes are connected to this node?
# This function should return a tuple (name of node, number of satisfied connected nodes).
def answer_eleven():
    peripheral_nodes = answer_nine()
    diameter = answer_eight()
    path_length_list = [list(nx.shortest_path_length(G, node).values()).count(diameter)
                        for node in peripheral_nodes]
    result_node_pos = path_length_list.index(max(path_length_list))
    return (peripheral_nodes[result_node_pos], path_length_list[result_node_pos])


# Question 12
# Suppose you want to prevent communication from flowing to the node that you found in the previous question
# from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the
# graph (you're not allowed to remove the node from the previous question or the center nodes)?
# This function should return an integer.
def answer_twelve():
    to_node = answer_eleven()[0]
    center_node = list(answer_ten())[0]
    return len(nx.minimum_node_cut(G, center_node, to_node))


# Question 13
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# This function should return a networkx Graph.
def answer_thirteen():
    G_un = nx.Graph(G.to_undirected())
    return G_un


# Question 14
# What is the transitivity and average clustering coefficient of graph G_un?
# This function should return a tuple (transitivity, avg clustering).
def answer_fourteen():
    G_un = answer_thirteen()
    return (nx.transitivity(G_un), nx.average_clustering(G_un))
print(answer_fourteen())
