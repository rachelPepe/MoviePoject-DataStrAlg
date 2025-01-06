# Graph class to create graph object
class Graph:
    def __init__(self):
        self.adjacency_list = {} # vertex dictionary {key:value}
        self.edge_weights = {} #edge dictionary {key:value}

    def add_vertex(self, new_vertex):
        # {vertex_1: [], vertex_2: [], ...}
        # adding key value pairs to dictionary
        #   - key = vertex_1 and value is [] empty list
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        # {(vertex_1,vertex_2): 484, (vertex_1, vertex_3): 626, ...}
        self.edge_weights[(from_vertex, to_vertex)] = weight
        # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}
        # adds to_vertex to the adjacency list of from_vertex
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
