# Prim is a greedy MST algorithm -> works well on dense graphs
# The algorithm must be run on connected graphs
# The lazy version of Prim's alg. has a runtime of 0(E*log(E))
from Graph import *
import queue as Q

def Prim_MST(graph):
    n = graph.count_nodes()
    pq = Q.PriorityQueue()
    visited = {node: False for node in graph.get_list_node()}
    start = graph.get_random_node()

    return lazyPrim(graph, start, n, pq, visited)

def lazyPrim(g, s, n, pq, visited):
    m = n - 1 # No of edges in MST
    edgeCount, mstCost = 0, 0
    mstEdges = []
    addEdges(g, s, visited, pq)

    while not pq.empty() and edgeCount != m:
        edge = pq.get() # O(log(E))
        nodeIndex = edge.get_to()

        if visited[nodeIndex]:
            continue # go back to the begining of the loop -> we take another edge from the pq

        weight = edge.get_weight()
        mstEdges.append(edge)
        edgeCount += 1
        mstCost += weight
        # We keep adding next edges to the pq
        addEdges(g, nodeIndex, visited, pq)
    if edgeCount != m:
        return None, None

    return mstCost, mstEdges

def addEdges(g, curr_node, visited, pq):
    # Mark the current node as visited
    visited[curr_node] = True
    edges_curr_node = g.get_node(curr_node).list_edges()

    for tmp in edges_curr_node:
        to = tmp.get_to() # get node to
        if not visited[to]:
            pq.put(tmp) # add the edge in the PriorityQueue (the comparison is wrt the edge's weight)
    pass

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

    #print(g.get_edge('a','b'))
    #print(type(g.get_node('a')))

    x, y = Prim_MST(g)
    print(f"Cost: {x}")
    print("Edges: ")
    for tmp in y:
        print(tmp, end = ' ')
    print()
    pass
