import networkx as nx
import pandas as pd
import numpy as np

# chess example
# We will be looking at chess_graph.txt, which is a directed graph of chess games in edge list format.
# Each node is a chess player, and each edge represents a game. The first column with an outgoing edge
# corresponds to the white player, the second column with an incoming edge corresponds to the black player.
# The third column, the weight of the edge, corresponds to the outcome of the game. A weight of 1 indicates
# white won, a 0 indicates a draw, and a -1 indicates black won.
# The fourth column corresponds to approximate timestamps of when the game was played.
# We can read in the chess graph using read_edgelist, and tell it to create the graph using a nx.MultiDiGraph.

chess = nx.read_edgelist('chess_graph.txt', data=[('outcome', int), ('timestamp', float)],
                         create_using=nx.MultiDiGraph())
print(chess.is_directed(), chess.is_multigraph())
print(chess.edges(data=True))

# use degree function to find how many games each player played
games_played = dict(chess.degree())
print(games_played)

# find the player with the max games played
max_value = max(games_played.values())
max_key = [i for i in games_played.keys() if games_played[i] == max_value]
print(max_key, max_value)

# find the player who has won the most games
# convert the edge list to a dataframe
df = pd.DataFrame(chess.edges(data=True),
                  columns=['white', 'black', 'outcome'])
print(df.head())
# extract the outcome value from the data dict
df['outcome'] = df['outcome'].map(lambda x: x['outcome'])
print(df.head())
# find the win as white count and win as black count
win_as_white = df[df['outcome']==1].groupby('white').sum()
win_as_black = -df[df['outcome']==-1].groupby('black').sum()
win_count = win_as_white.add(win_as_black, fill_value=0)
print(win_count.head())
# find the nlargest
print(win_count.nlargest(10, 'outcome'))
