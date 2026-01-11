import heapq
from visualize import Visualize

class ShortestPath:
    def __init__(self, vertices, num_of_edges, start_vertex, end_vertex, edges):
        self.vertices = vertices
        self.num_of_edges = num_of_edges
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.graph_edges = edges
        
        self.find_path()

    def find_path(self):
        self.final_weights_sum = 0
        self.final_edges_sum = 0
        self.final_path = None
        self.pq = []

        adjacents = {}

        for start_vertex, end_vertex, weight in self.graph_edges:
            if start_vertex not in adjacents:
                adjacents[start_vertex] = []

            adjacents[start_vertex].append((end_vertex, int(weight)))

        heapq.heappush(self.pq, (0, self.start_vertex))

        best = {self.start_vertex: 0}

        previous = {}

        while self.pq:
            current_weight, current_vertex = heapq.heappop(self.pq)

            if current_weight > best.get(current_vertex, float('inf')):
                continue

            if current_vertex == self.end_vertex:
                self.final_weights_sum = current_weight
                break

            for adjacent, adj_weight in adjacents.get(current_vertex, []):
                new_weight = current_weight + adj_weight

                if new_weight < best.get(adjacent, float('inf')):
                    best[adjacent] = new_weight
                    previous[adjacent] = current_vertex
                    heapq.heappush(self.pq, (new_weight, adjacent))

        if self.end_vertex not in best:
            print(f"No path found from ({self.start_vertex}) to ({self.end_vertex})")
            return

        path = []
        visited_vertex = self.end_vertex
        while visited_vertex != self.start_vertex:
            path.append(visited_vertex)
            visited_vertex = previous[visited_vertex]

        path.append(self.start_vertex)
        path.reverse()

        self.final_path = path
        self.final_edges_sum = len(path) - 1
        
        print(f"for the shortest path algorithm travels through {self.final_edges_sum} edges\nwith total sum of {self.final_weights_sum} weights\n({') --> ('.join(self.final_path)})")
        visualize = Visualize(self.vertices, self.graph_edges, self.final_path)