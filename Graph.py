# Class for (un)directed,(un)weighted graph
# Default: undirected and unweighted graph
import random

class Vertex:
    # Special class for the Graph node
    # The DS has the node id and the list of neighbors
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id)

    def get_id(self):
        return self.id

    def get_adj(self):
        return self.adjacent

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        try:
            return self.adjacent[neighbor]
        except:
            return f"No neighbor {neighbor}"

    def add_neighbor(self, t, weight = 0):
        self.adjacent[t] = weight

    def list_edges(self):
        edges = []
        for tmp in self.adjacent:
            edges.append(Edge(self.id, tmp, self.adjacent[tmp]))
        return edges

class Edge:
    # Special class for the Graph's edges
    # Edge is a triplet:
    # (From, To, Weight)
    def __init__(self, s, t, weight = 1):
        self.s = s
        self.t = t
        self.weight = weight

    def __str__(self):
        return f"({str(self.s)}, {str(self.t)}, {str(self.weight)})"

    def __lt__(self, other):
        # Comparison of edges wrt their weights
        return self.weight <= other.weight

    def get_from(self):
        return self.s

    def get_to(self):
        return self.t

    def get_weight(self):
        return self.weight

class Graph:
    def __init__(self, undirected = True):
        self.vertices = {} # dicionario com tipos primitivos (key) apontando para o tipo "Vertex" (Value)
        self.num_nodes = 0
        self.num_edges = 0
        self.undirected = undirected

    def count_nodes(self):
        return self.num_nodes

    def count_edges(self):
        return self.num_edges

    def add_node(self, node): # node é um tipo primitivo
        self.num_nodes += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex #lista com tipo Vertex

    def add_edge(self, s, t, cost = 0):
        if s not in self.vertices:
            self.add_node(s)
        if t not in self.vertices:
            self.add_node(t)

        self.vertices[s].add_neighbor(t,cost)
        self.num_edges += 1
        if self.undirected:
            self.vertices[t].add_neighbor(s, cost)
        pass

    def get_list_node(self):
        return list(self.vertices.keys()) #return list with the node's primitive type

    def get_list_edges(self):
        edges = []

        for node in self.vertices:
            for local_edges in self.vertices[node].list_edges():
                edges.append(local_edges)

        return edges

    def get_node(self, node): #node is primitive (Vertex's id)
        try:
            return self.vertices[node] #retorna the Vertex node
        except:
            return f"No such node: {node}"

    def get_random_node(self):
        aux = random.choice(list(self.vertices.values())) # return random Vertex
        return aux.get_id()

    def get_edge(self, s, t):
        if s not in self.vertices:
            return f"Node {s} not in graph"
        if t not in self.vertices:
            return f"Node {t} not in graph"

        return Edge(s, t, self.vertices[s].get_weight(t))

if __name__ == '__main__':
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')

    g.add_edge('a', 'b', 3)
    g.add_edge('b','c',10)

    print(g.get_edge('c','b'))
    print(g.get_random_node())
    for aux in g.get_node('b').list_edges():
        print(aux, end = ' ')
    print()
    for aux in g.get_node('a').list_edges():
        print(aux, end = ' ')
