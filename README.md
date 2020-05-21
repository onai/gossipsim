# Gossip Network Simulation

Allows modeling of gossip networks and obtaining various metrics associated with a gossip network with given parameters. As examples, we demonstrate experiments to get (a) the shortest path length for messages to reach randomly chosen destinations on a randomly generated network and (b) the average path length for messages sent in parallel to reach ⅔ of the nodes in a randomly generated network.

# Table Of Contents
1. [How To Run](#how-to-run)
2. [Sample results](#sample-results)
    - [Shortest Path Time in a Network](#shortest-path-time-in-a-network)
    - [Average time required for messages to reach ⅔ of the nodes](#average-time-required-for-messages-to-reach--of-the-nodes)
3. [References](#references)

# How to Run

Install requirements with `pip install requirements.txt`

To obtain results for an instance of a network, run `sim.py` as follows.

Usage:
`python sim.py <M> <N> <size> <ds> <de>`
M -  Number of desired nodes from source to destination (Length of path)

N - Number of entrypoints in the graph

size - Number of nodes in the graph

ds - Minimum degree of graph

de - Maximum degree of graph

Use the helper script to generate the experimental results described later in this README, as follows.

Usage:
`./run_experiment.sh`
Will generate a log file `log.txt` with all the data required to plot the graphs above. Vary M, N, ds, de, and size as needed

List of scripts used to plot graphs below:
`plot_m_avgd_sp.py` - Fig. 1
`plot_n_avgd_23.py` - Fig. 2
`plot_n_23.py` - Fig. 3
`plot_avg_23.py` - Fig. 4

# Sample results
## Shortest Path time in a network
With the tool, we performed analysis on graphs with 1000, 2000, 3000, 4000 and 5000 nodes, with the degree of each node selected from a uniform distribution ranging from 5 to 20. Each hop counts as one time unit.

First we consider the time required to send a message to a specific number of randomly specified nodes in a specified order. The message can only travel along edges in the graph. Therefore, we are interested in the shortest path from the source node to the first intermediate plus the shortest path from the first intermediate, from the first intermediate to the second intermediate, and so on until the final destination is reached. This scenario arises in many situations, including Tor or mix networks, where an encrypted message must be decrypted by a specific sequence of nodes [3].

To compute this, we first find the average all pairs shortest path length, which gives us the average time for one hop and then multiply that average by M, where M is the number of nodes in the desired path. We considered M values ranging from 2 to 5.

Figure 1 shows a plot of the path time compared against graph size, M, and average degree of the graph. Notice that the shortest time path does not vary significantly with the average degree. However, it does vary with higher average degrees than are shown in this plot, for example degrees greater than 100 per node (not shown for scaling reasons). As might be expected, M has the largest impact on message travel times.
Figure 1: Plot of shortest path time compared against graph size, M and average degree


## Average time required for messages to reach ⅔ of the nodes

Next, we consider the time for a message to propagate through the random gossip graph. In particular, we assume that a message is introduced at N randomly selected entry nodes in the graph and each node sends it (in parallel) to its neighbors, which in turn send the message (in parallel) to its neighbors, and so on. We compute the time required for the message to reach ⅔ of the total number of nodes in the graph. Just as in the previous example, each network hop counts as one time unit

We consider N values (entry points in the graph) of 1,2, 3, 10, and 100. 

To compute the time, our program follows the following procedure. After randomly selecting the N entry points, we compute the single source shortest path. Then we find the minimum number of hops needed to reach each non-entry-point node, from across all entry nodes. We now have the time required to reach each node. We sort these times and take the entry at the position index equal to ⅔ of number of nodes. This gives us the average time required to reach ⅔ of the nodes.

Figure 2 shows a plot of this propagation time compared to graph size, N, and average degree. Just as with the shortest time analysis, we noticed that the shortest time path does not vary at low degrees, but there is a difference between a degree of, say, 10, and 200 (Figure 4).



Figure 2: Plot of ⅔ network propagation compared against graph size, N, and average degree

Furthermore, in Figure 3, we can see how the time to propagate to ⅔ nodes varies with respect to N and graph size. 




Figure 3: Plot of ⅔ network propagation compared against graph size, and N


Figure 4 shows the ranges of average degree that has an effect on the network propagation time. It is for a network size of 1000 with N set to 3. In a network with average degree of 380+, we see that it just takes 1 time unit to reach ⅔ of the network.



Figure 4: Effects of average degree on the time to reach ⅔ network propagation




# References

[1] Demers, Alan; Greene, Dan; Hauser, Carl; Irish, Wes; Larson, John; Shenker, Scott; Sturgis, Howard; Swinehart, Dan; Terry, Doug (1987-01-01). Epidemic Algorithms for Replicated Database Maintenance. Proceedings of the Sixth Annual ACM Symposium on Principles of Distributed Computing. PODC '87. New York, NY, USA: ACM. pp. 1–12. doi:10.1145/41840.41841. ISBN 978-0897912396.

[2] https://en.wikipedia.org/wiki/Gossip_protocol

[3] https://en.wikipedia.org/wiki/Mix_network
