
# Is a SSSP algorithm - can fin the shortest path from one node to others
# Can be used to detect negative cycles
# Time complexity: O(E*V)
from Graph import *

def bellman_ford(graph, start = None):
    if start == None:
        start = graph.get_random_node()
        print(f"Starting node: {start}")

    n = graph.count_nodes()
    e = graph.count_edges()
    d = {node: float('inf') for node in graph.get_list_node()} # distance to each node
    d[start] = 0

    # Running this loop we find the best paths
    for i in range(n - 1):
        for edge in graph.get_list_edges():
            print(f"Edge: {edge}")
            print()
            # Relax the edge
            distance = d[edge.get_from()] + edge.get_weight()
            if distance < d[edge.get_to()]:
                d[edge.get_to()] = distance

    # To detect negative cycles we run the loop one more time
    for i in range(n - 1):
        for edge in graph.get_list_edges():
            distance = d[edge.get_from()] + edge.get_weight()
            # If we can relax once again is because we have a negative cycle
            if distance < d[edge.get_to()]:
                d[edge.get_to()] = float('-inf')

    return d

if __name__ == "__main__":
    G = Graph(undirected = False)
    # add nodes and edges
    G.add_edge(0, 1, 5)
    G.add_edge(1, 6, 60)
    G.add_edge(1, 5, 30)
    G.add_edge(1, 2, 20)
    G.add_edge(2, 3, 10)
    G.add_edge(3, 2, -15)
    G.add_edge(2, 4, 75)
    G.add_edge(4, 9, 100)
    G.add_edge(5, 4, 25)
    G.add_edge(5, 6, 5)
    G.add_edge(6, 7, -50)
    G.add_edge(7, 8, -10)
    G.add_edge(5, 8, 50)

    start = 0
    dist = bellman_ford(G, start = start)
    for k, v in dist.items():
        print(f"d({start}, {k}) = {v}")

    pass
