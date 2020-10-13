# The topological ordering is an ordering of the nodes in a DAG
# where for each edge from A-> B, node A appears before node B.
# The topological sort algorithm can find a topological ordering in O(V + E)
from Graph import *

def topSort(graph):
    n = graph.count_nodes()
    list_nodes = graph.get_list_node()
    visited = {} # Memory for visited nodes
    ordering = [-1 for i in range(n)] # vector that will contain the order
    for node in list_nodes:
        visited[node] = False
    index = n - 1

    for at in list_nodes:
        if not visited[at]:
            index = dfs(index, at, visited, ordering, graph) # Depth First Search :)

    return ordering

def dfs(i, at, visited, ordering, graph):
    visited[at] = True

    list_edges = graph.get_node(at).list_edges()
    for edge in list_edges:
        if not visited[edge.get_to()]:
            i = dfs(i, edge.get_to(), visited, ordering, graph)

    ordering[i] = at

    return i - 1

if __name__ == "__main__":
    # Only for directed acyclic graphs !
    G = Graph(undirected = False)

    G.add_node('e')
    G.add_node('b')
    G.add_node('d')
    G.add_node('a')
    G.add_node('c')

    G.add_edge('a', 'b')
    G.add_edge('a', 'e')
    G.add_edge('b', 'd')
    G.add_edge('b', 'c')
    G.add_edge('e', 'b')

    print(topSort(G))
    pass
