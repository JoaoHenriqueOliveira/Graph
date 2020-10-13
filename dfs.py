# Depth First Search
# Time Complexity: O(V + E)
# In DFS we visit all verties of a component region of the graph
import random

def DepthFirstSearch(graph):
    n = len(graph)
    visited = [False for i in range(n)]
    at = random.randint(0, n - 1) # Initial node

    dfs(at, visited, graph)
    pass

def dfs(at, visited, graph):
    if visited[at]:
        return
    else:
        print(f"{at} -> ", end = ' ')
        visited[at] = True

    neighbors = graph[at]
    for next in neighbors:
        dfs(next, visited, graph)
    pass

# Application of Depth First Search
def FindConnectedComponents(graph):
    n = len(graph)
    visited = [False for i in range(n)]
    count = 0
    components = [0 for i in range(n)]

    find_components(visited, n, count, components, graph)
    pass

def find_components(visited, n, count, components, graph):
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs_component(i, count, visited, components, graph)

    print(f"Components: {count}")
    for node in graph:
        print(f"Node: {node} -> Component: {components[node]}")

    return (count, components)

def dfs_component(node, count, visited, components, graph):
    visited[node] = True
    components[node] = count
    neighbors = graph[node]

    for next in neighbors:
        if not visited[next]:
            dfs_component(next, count, visited, components, graph)

    pass

if __name__ == "__main__":
    graph = {0: [9, 1], 1: [0, 8], 2: [3], 3: [2, 4, 5, 7], 4: [3], 5: [3, 6], 6: [5, 7], 7: [8, 3, 6, 10, 11], 8: [1, 9, 7], 9: [0, 8], 10: [7, 11],
             11: [10, 7], 12: []}
    # DepthFirstSearch(graph)
    FindConnectedComponents(graph)
    print()

    pass
