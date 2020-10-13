# SSSP = Single Source Shortest Path
# To be solved on a DAG. Time complexity: O(V + E)

from Graph import *
from top_sort import topSort

def sssp(graph):
    top_order = topSort(graph) # Get list of the DAG's Topological Ordering
    distances = {node: float("inf") for node in top_order}
    first  = True

    for node in top_order:
        if first:
            distances[top_order[0]] = 0
            first = False

        for neighbor in graph.get_node(node).get_neighbors():
            w = graph.get_edge(node, neighbor).get_weight()
            d = w + distances[node]
            if d < distances[neighbor]:
                distances[neighbor] = d

    return distances

if __name__ == "__main__":
    G = Graph(undirected = False) # G must be a DAG!

    G.add_node('e')
    G.add_node('b')
    G.add_node('d')
    G.add_node('a')
    G.add_node('c')

    G.add_edge('a', 'b', 3)
    G.add_edge('a', 'e', 4)
    G.add_edge('b', 'd', 8)
    G.add_edge('b', 'c', 700)
    G.add_edge('e', 'b', -5)
    G.add_edge('e', 'd', -20)
    G.add_edge('a', 'c', 2)

    list_of_distances = sssp(G)

    for k, v in list_of_distances.items():
        print(f"d(ancestor, {k}) = {v}")

    pass
