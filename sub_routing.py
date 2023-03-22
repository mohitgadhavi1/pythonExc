import networkx as nx

# create a graph representing the network
G = nx.Graph

# add nodes to the graph representing sub-networks
G.add_nodes_from(['A','B','C'])

# add edges to the graph representing connections between sub-networks
G.add_edges_from([("A","B"),("B","C")])


# create sub-graphs representing each sub-network
subgraphs = {node : G.subgraph(nx.node_connected_component(G, node)) for node in G.nodes }

# define the source and destination for the packets
source = "A"
destination = "C"

# find the shortest path between the source and destination using sub-routing
path = nx.shortest_path(subgraphs[source],source,destination)


# output the path taken by the packets
print(path)