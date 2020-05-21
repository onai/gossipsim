from gen import *
import networkx as nx
import time
import numpy as np
import math
import argparse
import sys


def shortest_path(G, M=10):

    """
    G - graph
    M - number of nodes in the mix network
    N - number of mix paths
    
    Shortest path across mix network: Pick random nodes and find shortest path between them
    multiply the time take by M

    """

    return nx.average_shortest_path_length(G) * M


def reach(G, N=3):

    """
    G - graph
    M - number of nodes in the mix network
    N - number of mix paths

    Start from N sources. Start with source 1, do BFS till exhaustion and take note of depth to reach a child.
    Start with source 2 till N and if depth of a node is lesser than before, update it. Need minimum depth.

    """

    Gnodes = list(G.nodes)
    sources = np.random.choice(Gnodes, N)
    sssp_length = []

    for source in sources:
        sssp_length.append(nx.single_source_shortest_path_length(G, source))

    min_dict = {}

    for key in sssp_length[0]:
        seq = [x[key] for x in sssp_length]
        min_dict[key] = min(seq)

    idx_23 = int(math.ceil((2.0/3.0) * len(Gnodes)))
    return sorted(min_dict.values())[idx_23]



if __name__== "__main__":

    M = int(sys.argv[1])
    N = int(sys.argv[2])
    size = int(sys.argv[3])
    ds = int(sys.argv[4])
    de = int(sys.argv[5])

    print("Generating for")
    print(sys.argv)

    G = generate_graph(ds, de, size)

    # check degreee
    # d = [G.degree[i] for i in range(len(G.degree))]

    # to numpy
    # Gm = nx.to_numpy_array(G)

    # shortest_path
    time_sp = shortest_path(G, M)

    # time for message to reach 2/3rd of the network
    time_23 = reach(G, N)


    print("M mix shortest path time: ", time_sp)
    print("Time to reach 2/3 nodes: ", time_23)
    print("-_-_-_-_-_-_-_-_done-_-_-_-_-_-_-_-_")

