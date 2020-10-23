from Graph import *
import queue

def Ford_Fulkerson(graph, s, t, write = True):
    n = graph.count_nodes()
    max_flow = 0


    while has_augmenting_path(graph):
        bottle_neck, path = find_augmenting_path(graph, n, s, t)
        update_aug_path(graph, path, visited)
        max_flow += bottle_neck

    if write:
        write_network(graph)

    return max_flow

def find_augmenting_path(graph, n, s, t):
    prev = bfs(graph, n, s)
    return build_path(prev, s, t, n)

def bfs(graph, n, s):
    q = queue.Queue()
    q.put(s)
    prev = [-1 for i in range(n)]
    visited = {node: False for node in graph.get_list_node()}
    visited[s] = True

    while not q.empty():
        next = q.get()
        neighbors = graph[next]

        for elem in neighbors:
            if not visited[elem] and graph.get_edge(s, elem).

        pass


    pass

def build_path(prev, s, t, n):
    pass

def update_augmenting_path(graph, path, visited):
    pass

if __name__ == '__main__':
    pass
