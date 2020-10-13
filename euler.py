#Directed Graph
#O(E)
def coun_edges(graph):
    count = 0
    for node in graph:
        count += len(graph[node])
    return count

def EulerianPath(graph):
    n = len(graph)
    in_deg = [0 for i in range(n)]
    out_deg = [0 for i in range(n)]
    path = []
    
    return FindEulerianPath(in_deg, out_deg, graph, n, path)

def FindEulerianPath(in_deg, out_deg, graph, n, path):
    m = coun_edges(graph)
    in_deg, out_deg = CountInOutDegree(in_deg, out_deg, graph)
    
    if not HasEulerianPath(in_deg, out_deg, n):
        return -1
    
    start = findStartNode(in_deg, out_deg, n)
    path = dfs(start, in_deg, out_deg, graph, path)
    
    if len(path) == m + 1:
        return path[::-1]
        
    return -1

def findStartNode(in_deg, out_deg, n):
    start = 0
    
    for i in range(n):
        if out_deg[i] - in_deg[i] == 1:
            return i
        if out_deg[i] > 0:
            start = i
    
    return start

def dfs(at, in_deg, out_deg, graph, path):
    
    while out_deg[at] != 0:
        next = graph[at][out_deg[at] - 1]
        out_deg[at] -= 1
        dfs(next, in_deg, out_deg, graph, path)
    
    path.append(at)
    
    return path


def CountInOutDegree(in_deg, out_deg, graph):
    
    for node in graph:
        adj = graph[node]
        for next in adj:
            in_deg[next] += 1
            out_deg[node] += 1
    
    return in_deg, out_deg

def HasEulerianPath(in_deg, out_deg, n):
    start, end = 0, 0
    
    for i in range(n):
        if(out_deg[i] - in_deg[i] > 1) or (in_deg[i] - out_deg[i] > 1):
            return False
        elif out_deg[i] - in_deg[i] == 1:
            start += 1
        elif in_deg[i] - out_deg[i] == 1:
            end += 1
    
    return (end == 0 and start == 0) or (end == 1 and start == 1)

if __name__ == "__main__":
    
    #graph = {0: [], 1: [2,3], 2: [2, 4, 4], 3: [1, 2, 5], 4: [3, 6], 5: [6], 6: [3]}
    graph = {0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}
    print(EulerianPath(graph))
    pass