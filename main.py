from ChainingHashTable import ChainingHashTable
from Movie import Movie
from Graph import Graph
from Vertex import Vertex
import csv


# ---------- Code to load movie data from csv file and fetch --------------------
def loadMovieData(filename):
    with open(filename) as best_movies:
        movie_data = csv.reader(best_movies, delimiter=',')
        next(movie_data) # skip header
        for movie in movie_data:
            m_ID = int(movie[0])
            m_title = movie[1]
            m_year = movie[2]
            m_price = movie[3]
            m_city = movie[4]
            m_state = movie[5]
            m_status = 'Loaded'

            # movie object
            movie = Movie(m_ID, m_title, m_year, m_price, m_city, m_state, m_status)

            # insert into the hash table
            movie_hash.insert(m_ID, movie)

# hash table instance
movie_hash = ChainingHashTable()

# load movie into hash table
loadMovieData('BestMovies.csv')

# fetch data from hash table
print("Uploaded movie list of top 11 movies in 2025")
for i in range(len(movie_hash.table) + 1):
    print("Key: {} and Movie: {}".format(i+1, movie_hash.search(i+1)))
print("")
print("")

# ----------------- Dijkstra's shortest path functions  ________________________________
# determines shortest path from start vertex to each vertex in a graph
# for each vertex this alg determines the vertexes distance and predecessor pointers with
#   the distance being the shortest path distance from the start vertex and predecessor
#   pointer points to previous vertex along the shortest path from start vertex
def dijkstra_shortest_path(g, start_vertex):
    # put all vertices in an unvisited que
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        # unvisited_queue = [vertex_1, vertex_2, ...]
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # one vertex is removed with each iteration; repeat until the list is empty
    while (len(unvisited_queue)) > 0:

        # visit vertex with min distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        print(f"\nProcessing vertex {current_vertex.label}:")
        print(f"Current distance: {current_vertex.distance}")

        # check potential path lengths from the current vertex to all neighbors
        for adj_vertex in g.adjacency_list[current_vertex]: # values from directory
            # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3],
            # if vertex_2 => adj_vertex in [vertex_6], ...
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)] # values from directory
            # edge weight = 484 then 626 then 1306, ...}
            alternative_path_distance = current_vertex.distance + edge_weight
            # if shorter path from start_vertex to adj_vertex is found update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex

        print("\nUnvisited Queue after this iteration:")
        for vertex in unvisited_queue:
            print(f"{vertex.label}: distance={vertex.distance}, "
                f"predecessor={vertex.pred_vertex.label if vertex.pred_vertex else None}")
        print("")

'''
Example Walkthrough

Let’s assume the graph has the following:
start_vertex = vertex_1
vertex_1.distance = 0
All other vertices: .distance = inf
unvisited_queue = [vertex_1, vertex_2, ..., vertex_11]

Iteration 1
Current Vertex: vertex_1
vertex_1.distance = 0
Neighbors:
vertex_2:
    alt = 0 + 484 = 484
    Update:
        vertex_2.distance = 484
        vertex_2.pred_vertex = vertex_1.
vertex_3:
    alt = 0 + 626 = 626
    Update:
        vertex_3.distance = 626
        vertex_3.pred_vertex = vertex_1.
State After Updates:
    unvisited_queue = [vertex_2, vertex_3, ..., vertex_11]
    distances = {1: 0, 2: 484, 3: 626, 4: inf, ..., 11: inf}


Iteration 2
Current Vertex: vertex_2
vertex_2.distance = 484
Neighbors:
vertex_6:
    alt = 484 + 1306 = 1790
    Update:
        vertex_6.distance = 1790
        vertex_6.pred_vertex = vertex_2.
State After Updates:
    unvisited_queue = [vertex_3, vertex_6, ..., vertex_11]
    distances = {1: 0, 2: 484, 3: 626, 4: inf, 5: inf, 6: 1790, ..., 11: inf}


Iteration 3
Current Vertex: vertex_3
vertex_3.distance = 626
Neighbors:
vertex_5:
    alt = 626 + 774 = 1400
    Update:
        vertex_5.distance = 1400
        vertex_5.pred_vertex = vertex_3.
vertex_4:
    alt = 626 + 687 = 1313
    Update:
        vertex_4.distance = 1313
        vertex_4.pred_vertex = vertex_3.
State After Updates:
    unvisited_queue = [vertex_4, vertex_5, vertex_6, ..., vertex_11]
    distances = {1: 0, 2: 484, 3: 626, 4: 1313, 5: 1400, 6: 1790, ..., 11: inf}
'''

def get_shortest_path(start_vertex, end_vertex):
    # start from end_vertex and build the path backwards
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path

def get_shortest_path_city(start_vertex, end_vertex):
    # start from end_vertex and build the path backwards
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        my_movie_obj = movie_hash.search(int(current_vertex.label))
        path = " -> " + my_movie_obj.city + path
        current_vertex = current_vertex.pred_vertex
    path = "Los Angeles " + path
    return path


# _______________ Dijkstras shortest path main ________________________________________-
# program to find the shortest paths from vertex A

g = Graph()

# add Vertices
vertex_1 = Vertex('1')
g.add_vertex(vertex_1)
vertex_2 = Vertex('2')
g.add_vertex(vertex_2)
vertex_3 = Vertex('3')
g.add_vertex(vertex_3)
vertex_4 = Vertex('4')
g.add_vertex(vertex_4)
vertex_5 = Vertex('5')
g.add_vertex(vertex_5)
vertex_6 = Vertex('6')
g.add_vertex(vertex_6)
vertex_7 = Vertex('7')
g.add_vertex(vertex_7)
vertex_8 = Vertex('8')
g.add_vertex(vertex_8)
vertex_9 = Vertex('9')
g.add_vertex(vertex_9)
vertex_10 = Vertex('10')
g.add_vertex(vertex_10)
vertex_11 = Vertex('11')
g.add_vertex(vertex_11)

# add edges
g.add_undirected_edge(vertex_1, vertex_2, 484)
g.add_undirected_edge(vertex_1, vertex_3, 626)
g.add_undirected_edge(vertex_2, vertex_6, 1306)
g.add_undirected_edge(vertex_3, vertex_5, 774)
g.add_undirected_edge(vertex_3, vertex_4, 687)
g.add_undirected_edge(vertex_4, vertex_11, 797)
g.add_undirected_edge(vertex_5, vertex_6, 482)
g.add_undirected_edge(vertex_6, vertex_7, 936)
g.add_undirected_edge(vertex_7, vertex_8, 535)
g.add_undirected_edge(vertex_7, vertex_9, 504)
g.add_undirected_edge(vertex_9, vertex_10, 594)
g.add_undirected_edge(vertex_11, vertex_5, 970)
g.add_undirected_edge(vertex_11, vertex_8, 664)
g.add_undirected_edge(vertex_11, vertex_9, 567)
g.add_undirected_edge(vertex_11, vertex_10, 453)

# Run Dijkstra's algorithm first
print("Program running dijkstra's shortest path to determine the shortest distance from each ")
print("vertex(city) to the starting city, as well as each vertex's predecessor on that path")
dijkstra_shortest_path(g, vertex_1)

# get the vertices by the label for convenience; display shortest path for each vertex from vertex_1
print("\nDijkstra shortest path:")
for v in g.adjacency_list:
    if v.pred_vertex is None and v  is not vertex_1:
        print(f'1 to {v.label} ==> no path exists')
    else:
        print(f'1 to {v.label} {get_shortest_path(vertex_1, v)} (total distance: {v.distance})')
print("")


print("Adjacency list:")
for vertex, neighbors in g.adjacency_list.items():
    print(f"{vertex} -> {[str(neighbor) for neighbor in neighbors]}")
print("")






