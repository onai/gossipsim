import random 
import networkx as nx


# generate a random graph with degree between a and b
def generate_graph(degree_start=10, degree_end=15, size=5000):

    z=[random.randint(degree_start, degree_end) for i in range(size)]

    # if sum of degree sequence is odd, make it even
    if sum(z) % 2 != 0:
       z[random.randint(0, size)] += 1 

    G=nx.configuration_model(z)

    # remove self-loops and parallel edges
    G=nx.Graph(G)
    G.remove_edges_from(G.selfloop_edges())

    return G



def generate_graph_mean(degree_start=10, degree_end=15, size=5000):

    z=[numpy.random.geometric(0.07) for i in range(size)]

    print("Mean degree", numpy.mean(z))
    # if sum of degree sequence is odd, make it even
    if sum(z) % 2 != 0:
       z[random.randint(0, size)] += 1

    G=nx.configuration_model(z)

    # remove self-loops and parallel edges
    G=nx.Graph(G)
    G.remove_edges_from(G.selfloop_edges())

    return G
