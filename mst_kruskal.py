# Implementation of Kruskal algorithm
# Runtime complexity: O(N*E*log(E))
from Graph import *

def Kruskal_MST(graph):
    n = graph.count_nodes()
    visited = {}
    for node in graph.get_list_node():
        visited[node] = False
    sorted_edges = []

    for node in graph.get_list_node():
        vertex = graph.get_node(node)
        out_edges = vertex.list_edges()
        for tmp in out_edges:
            sorted_edges.append(tmp)
    sorted_edges.sort()

    return kruskal_procedure(graph, n, visited, sorted_edges)

def kruskal_procedure(graph, n, visited, sorted_edges):
    m = n - 1
    mst_cost, count_edges = 0, 0
    mst_edges = []
    first = True

    while len(sorted_edges) != 0 and count_edges != m:
        edge = sorted_edges.pop(0)

        if first:
            frm = edge.get_from()
            visited[frm] = True
            first = False

        to = edge.get_to()
        if not visited[to]:
            visited[to] = True
            count_edges += 1
            mst_cost += edge.get_weight()
            mst_edges.append(edge)

    if count_edges != m:
        return None, None
    return mst_cost, mst_edges

if __name__ == '__main__':
    g = Graph()
    # add nodes
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)

    # add edges
    g.add_edge(0,1,2)
    g.add_edge(0,3,2)
    g.add_edge(0,2,5)
    g.add_edge(0,4,3)
    g.add_edge(1,3,0)
    g.add_edge(2,4,6)
    g.add_edge(2,3,1)
    g.add_edge(3,4,4)
    g.add_edge(3,5,8)

    cost, edges = Kruskal_MST(g)
    print(f"Cost: {cost}")
    print("Edges: ")
    for tmp in edges:
        print(tmp, end = ' ')
    print()
    pass




    pass
