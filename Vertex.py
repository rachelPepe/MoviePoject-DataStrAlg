# Vertex class - used in the shortest path algorithm
class Vertex:
    # constructor for a new Vertex object
    # starts with a distance of positive infinity
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

    def __repr__(self):
        return f"Vertex({self.label})"

    def __str__(self):
        return f'Vertex:(label={self.label}, distance={self.distance}, predecessor={self.pred_vertex.label if self.pred_vertex else None})'


