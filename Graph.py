# Class for (un)directed,(un)weighted graph
# Network Graph suppport
# Default: undirected and unweighted graph (Network = False)
import random


class Vertex:
    # Special class for the Graph node
    # The DS has the node id and the list of neighbors
    # For Network Graph the adjacent list has the [Weight, Flow] - pair for the corresponding neighbor as value
    def __init__(self, node, network=False):
        self.id = node
        self.adjacent = {}
        self.network = network

   def __str__(self):
        return str(self.id)

    def get_id(self):
        return self.id

    def get_adj(self):
        return self.adjacent

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        if not self.network:
            return self.adjacent[neighbor]
        elif self.network:
            return self.adjacent[neighbor][0]
        else:
            return f"No neighbor {neighbor}"

    def get_flow(self, neighbor):
        if self.network:
            return self.adjacent[neighbor][1]
        else:
            return "Not a network graph"

    def get_remaining_capacity(self, neighbor):
        if self.network:
            return self.adjacent[neighbor][0] - self.adjacent[neighbor][1]
        else:
            return "Not a network graph"

    def add_neighbor(self, t, weight=0, flow=0):
        if not self.network:
            self.adjacent[t] = weight
        else:
            self.adjacent[t] = [weight, flow]
        pass

    def add_flow(self, t, var):
        if not self.network:
            return "Not a Network"
        else:
            new_flow = self.adjacent[t][1] + var
            if new_flow > self.adjacent[t][0]:
                return "Overflow!"
            else:
                self.adjacent[t][1] = new_flow
        pass

    def list_edges(self):
        edges = []
        for tmp in self.adjacent:
            edges.append(Edge(self.id, tmp, self.adjacent[tmp]))

        return edges


class Edge:
    # Special class for the Graph's edges
    # Edge is a triplet:
    # (From, To, Weight)
    def __init__(self, s, t, weight=0):
        self.s = s
        self.t = t
        self.weight = weight  # weight = capacity in case of network

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
    def __init__(self, undirected=True, network=False):
        # dicionario com tipos primitivos (key) apontando para o tipo "Vertex" (Value)
        self.vertices = {}
        self.num_nodes = 0
        self.num_edges = 0
        self.undirected = undirected
        self.network = network

    def is_undirected(self):
        return self.undirected

    def is_network(self):
        return self.network

    def get_list_node(self):
        # return list with the node's primitive type
        return list(self.vertices.keys())

    def get_list_edges(self):
        edges = []

        for node in self.vertices:
            for local_edges in self.vertices[node].list_edges():
                edges.append(local_edges)

        return edges

    def get_node(self, node):  # node is primitive (Vertex's id)
        try:
            return self.vertices[node]  # retorna the Vertex node
        except:
            return f"No such node: {node}"

    def get_random_node(self):
        aux = random.choice(list(self.vertices.values())
                            )  # return random Vertex
        return aux.get_id()

    def get_edge(self, s, t):
        if s not in self.vertices:
            return f"Node {s} not in graph"
        if t not in self.vertices:
            return f"Node {t} not in graph"
        # if self.network:
            # return Edge(s, t, self.vertices[s].get_weight)

        return Edge(s, t, self.vertices[s].get_weight(t))

    def count_nodes(self):
        return self.num_nodes

    def count_edges(self):
        return self.num_edges

    def add_node(self, node):  # node é um tipo primitivo
        self.num_nodes += 1
        if self.network:
            new_vertex = Vertex(node, network=self.network)
            self.vertices[node] = new_vertex
            return

        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex  # lista com tipo Vertex
        pass

    def add_edge(self, s, t, weight=0):  # add edge s -> t
        if s not in self.vertices:
            self.add_node(s)
        if t not in self.vertices:
            self.add_node(t)

        if self.network:
            self.vertices[s].add_neighbor(t, weight)
            self.num_edges += 1
            # add residual edge (t -> s): capacity = 0, flow = 0 (Default)
            self.vertices[t].add_neighbor(s)
            return

        self.vertices[s].add_neighbor(t, weight)
        self.num_edges += 1

        if self.undirected:
            self.vertices[t].add_neighbor(s, cost)

        pass


if __name__ == '__main__':
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')

    g.add_edge('a', 'b', 3)
    g.add_edge('b', 'c', 10)

    print(g.get_edge('c', 'b'))
    print(g.get_random_node())
    for aux in g.get_node('b').list_edges():
        print(aux, end=' ')
    print()
    for aux in g.get_node('a').list_edges():
        print(aux, end=' ')
