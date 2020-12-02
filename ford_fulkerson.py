# Network max flow solver
# uses Edmonds-Karp heuristic: O(VE²)
# trasnverse the graph using BFS until there is no more augmenting paths
from Graph import *
import queue


def Ford_Fulkerson(graph, s, t, write_flow=True):
    max_flow = 0

    while has_augmenting_path(graph, s):
        print(max_flow)
        path, bottle_neck = find_augmenting_path(graph, s, t)
        update_augmenting_path(graph, path, bottle_neck)
        max_flow += bottle_neck

    if write_flow:
        print("Summary (residual graph):")
        write(graph, s, t)

    return max_flow


def has_augmenting_path(graph, s):
    src = graph.get_node(s)
    neighbors = src.get_neighbors()

    for adj in neighbors:
        if src.get_remaining_capacity(adj):
            return True

    return False


def find_augmenting_path(graph, s, t):
    prev = bfs(graph, s, t)
    return build_path(graph, prev, s, t)


def bfs(graph, s, t):
    q = queue.Queue()
    q.put(s)
    prev = {node: -1 for node in graph.get_list_node()}
    visited = {node: False for node in graph.get_list_node()}
    visited[s] = True

    while not q.empty():
        next = q.get()
        if next == t:
            break
        neighbors = graph.get_node(next).get_neighbors()

        for elem in neighbors:
            if not visited[elem] and graph.get_node(next).get_remaining_capacity(elem) > 0:
                q.put(elem)
                visited[elem] = True
                prev[elem] = next

    return prev


def build_path(graph, prev, start, end):
    path = []
    bottle_neck = float('inf')
    capacity = float('inf')

    at = end
    while at != -1:
        tmp = at
        path.append(at)
        at = prev[at]
        if at != -1:
            capacity = graph.get_node(at).get_remaining_capacity(tmp)
        if bottle_neck > capacity:
            bottle_neck = capacity

    path.reverse()
    if path[0] == start:
        print(path)
        print(f"bottleneck: {bottle_neck}")
        return path, bottle_neck

    print("No path")
    return [], float('inf')


def update_augmenting_path(graph, path, bottle_neck):
    m = len(path)
    index = 0

    while index < m - 1:
        node = path[index]
        # update remaining capacity
        graph.get_node(node).add_flow(path[index + 1], bottle_neck)
        graph.get_node(path[index + 1]).add_flow(node, -
                                                 bottle_neck)  # update residual edge
        index += 1
    pass


def write(graph, s, t):
    print(f"Source: {s}")

    for node in graph.get_list_node():
        vertex = graph.get_node(node)
        for neighbor in vertex.get_neighbors():
            print(
                f"From: {node} \t To: {neighbor} \t Flow: {vertex.get_flow(neighbor)} \t Capacity: {vertex.get_remaining_capacity(neighbor)}")

    print(f"Sink: {t}")
    return


if __name__ == '__main__':
    g = Graph(network=True)
    # add num_nodes
    g.add_node('s')

    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)

    g.add_node('t')
    # add num_edges
    g.add_edge('s', 0, 5)
    g.add_edge('s', 1, 10)
    g.add_edge('s', 2, 5)
    g.add_edge(0, 3, 10)
    g.add_edge(1, 0, 15)
    g.add_edge(1, 4, 20)
    g.add_edge(2, 5, 10)
    g.add_edge(3, 4, 25)
    g.add_edge(3, 6, 10)
    g.add_edge(4, 2, 5)
    g.add_edge(4, 7, 30)
    g.add_edge(5, 7, 5)
    g.add_edge(5, 8, 10)
    g.add_edge(6, 't', 5)
    g.add_edge(7, 't', 15)
    g.add_edge(7, 3, 15)
    g.add_edge(7, 8, 5)
    g.add_edge(8, 't', 10)

    flow = Ford_Fulkerson(g, 's', 't')
    print(f"Max Flow: {flow}")
    pass
