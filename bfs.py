# Breadth First Search
# Time complexty: O(E + V)
import queue
import random
# BFS starting at node

def BFS(graph):
    n = len(graph)
    start = random.randint(0, n - 1)

    return BreadthFirstSearch(start, n, graph)

def BreadthFirstSearch(node, n, graph):
    q = queue.Queue()
    q.put(node)
    print(node, end = ' ')
    visited = [False for i in range(n)]
    visited[node] = True
    prev = [-1 for i in range(n)] # track the parent of each node, this is to help reconstruct the path

    while not q.empty():
        next = q.get()
        neighbors = graph[next]

        for elem in neighbors:
            if not visited[elem]:
                print(elem, end = ' ')
                q.put(elem)
                visited[elem] = True
                prev[elem] = next
    print()
    return prev

# Application: path finding
def FindPath(graph, s, e):
    n = len(graph)
    FindPath_bfs(s, e, graph, n)
    pass

def FindPath_bfs(start, end, graph, n):
    prev = BreadthFirstSearch(start, n, graph)

    return reconstruct_path(start, end, prev, n)

def reconstruct_path(start, end, prev, n):
    path = []

    at = end
    while at != -1:
        path.append(at)
        at = prev[at]

    path.reverse()
    if path[0] == start:
        print(path)
        return path

    return []


if __name__ == "__main__":
    graph = {0: [9, 7, 11], 1: [10, 8], 2: [12, 3], 3: [2, 4, 7], 4: [3], 5: [6], 6: [5, 7],
             7: [6, 3, 11, 0], 8: [1, 12, 9], 9: [10, 8, 0], 10: [9, 1], 11: [0, 7], 12: [8, 2]}
    s = 0
    e = 5
    FindPath(graph, s, e)
    pass
