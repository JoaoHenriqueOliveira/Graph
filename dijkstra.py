# Is a single source shortest path alg with non-negative edges weights.
# Runtime complexity: O(E*log(V))
# We use a heap to store the best next node
import queue as Q
from Graph import *

def lazy_dijkstra(graph, start = None):
    # Lazy because we iterate through all the heap elements
    if start == None:
        start = graph.get_random_node()

    n = graph.count_nodes()
    visited = {node: False for node in graph.get_list_node()}
    dist = {node: float("inf") for node in graph.get_list_node()}
    dist[start] = 0

    pq = Q.PriorityQueue() # to keep track of the best next node
    # (node distance, node_id) to properly assign a priority wrt the distance
    pq.put((0, start)) # initial node

    while not pq.empty():
        minValue, node_id = pq.get()
        visited[node_id] = True

        for edge in graph.get_node(node_id).list_edges():
            if visited[edge.get_to()]:
                continue
            new_dist = dist[node_id] + edge.get_weight()
            if new_dist < dist[edge.get_to()]:
                dist[edge.get_to()] = new_dist
                pq.put((new_dist, edge.get_to()))

    return dist

if __name__ == "__main__":
    G = Graph(undirected = False)
    '''
    G.add_node('e')
    G.add_node('b')
    G.add_node('d')
    G.add_node('a')
    G.add_node('c')

    G.add_edge('a', 'b', 3)
    G.add_edge('a', 'e', 1)
    G.add_edge('b', 'd', 8)
    G.add_edge('b', 'c', 7)
    G.add_edge('e', 'b', 1)
    '''
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)

    G.add_edge(0, 1, 4)
    G.add_edge(0, 2, 1)
    G.add_edge(2, 1, 2)
    G.add_edge(1, 3, 1)
    G.add_edge(2, 3, 5)
    G.add_edge(3, 4, 3)

    start = 0
    distances = lazy_dijkstra(G, start = start)
    for k, v in distances.items():
        print(f"d({start}, {k}) = {v}")

    pass
