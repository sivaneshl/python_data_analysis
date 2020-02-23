# Assignment 1 - Creating and Manipulating Graphs
# Eight employees at a small company were asked to choose 3 movies that they would most enjoy watching
# for the upcoming company movie night. These choices are stored in the file Employee_Movie_Choices.txt.
# A second file, Employee_Relationships.txt, has data on the relationships between different coworkers.
# The relationship score has value of -100 (Enemies) to +100 (Best Friends). A value of zero means the
# two employees haven't interacted or are indifferent.
# Both files are tab delimited.

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite

# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])

# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])


# Question 1
# Using NetworkX, load in the bipartite graph from Employee_Movie_Choices.txt and return that graph.
# This function should return a networkx graph with 19 nodes and 24 edges
def answer_one():
    movie_choice_df = pd.read_csv('../resources/Employee_Movie_Choices.txt', delimiter='\t',
                               skiprows=1, names=['Employee', 'Movie'])
    movie_choice_G = nx.from_pandas_edgelist(movie_choice_df, 'Employee', 'Movie')
    # print(len(movie_choice_G.edges()), len(movie_choice_G.nodes()))
    return movie_choice_G


# Question 2
# Using the graph from the previous question, add nodes attributes named 'type' where movies
# have the value 'movie' and employees have the value 'employee' and return that graph.
# This function should return a networkx graph with node attributes {'type': 'movie'} or {'type': 'employee'}
def answer_two():
    movie_choice_G = answer_one()
    for node in movie_choice_G.nodes():
        if node in employees:
            movie_choice_G.add_node(node, type='employee')
        elif node in movies:
            movie_choice_G.add_node(node, type='movie')

    # print(movie_choice_G.nodes(data=True))
    return movie_choice_G


# Question 3
# Find a weighted projection of the graph from answer_two which tells us how many movies different
#  pairs of employees have in common.
# This function should return a weighted projected graph.
def  answer_three():
    movie_choice_G = answer_two()
    p = bipartite.weighted_projected_graph(movie_choice_G, employees)
    return p


# Question 4
# Suppose you'd like to find out if people that have a high relationship score also like the same types of movies.
# Find the Pearson correlation ( using DataFrame.corr() ) between employee relationship scores and the number of
# movies they have in common. If two employees have no movies in common it should be treated as a 0,
# not a missing value, and should be included in the correlation calculation.
# This function should return a float.
def set_value(val):
    if val is np.nan:
        return {'weight': 0}
    else:
        return val

def answer_four():
    movie_G = answer_three()
    movies_df = pd.DataFrame(movie_G.edges(data=True), columns=['from', 'to', 'movie_score'])
    relation_G = nx.read_edgelist('../resources/Employee_Relationships.txt', data=[('relation_score', int)])
    relation_df = pd.DataFrame(relation_G.edges(data=True), columns=['from', 'to', 'relation_score'])

    movie_reverse_df = movies_df.copy()
    movie_reverse_df.rename(columns={"from": "temp", "to": "from"}, inplace=True)
    movie_reverse_df.rename(columns={"temp": "to"}, inplace=True)

    movie_final_df = pd.concat([movies_df, movie_reverse_df], sort=True)

    final_df = pd.merge(movie_final_df, relation_df, on=['from', 'to'], how='right')

    final_df['movie_score'] = final_df['movie_score'].map(set_value)
    final_df['movie_score'] = final_df['movie_score'].map(lambda x: x['weight'])
    final_df['relation_score'] = final_df['relation_score'].map(lambda x: x['relation_score'])
    value = final_df['movie_score'].corr(final_df['relation_score'])
    print(value)
    return value


answer_four()


