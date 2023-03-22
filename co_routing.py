import networkx as nx

# create a graph representing the network
G = nx.Graph()

# add nodes to the graph representing network devices
G.add_nodes_from([1,2,3,4])

# add edges to the graph representing network connections
G.add_edges_from([(1,2),(2,3),(2,4)])

# define the source and destination for the packets
source = 1
destination = 4

# find the shortest path between the source and destination using co-routing
path = nx.shortest_path(G,source,destination)

# output the path taken by the packets
print(path)