import heapq

class ShortestPath:
    def __init__(self, vertices, num_of_edges, start_vertex, end_vertex, edges):
        self.vertices = vertices
        self.num_of_edges = num_of_edges
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.graph_edges = edges
        
        self.find_path(edges)

    def find_path(self, edges):
        final_weights_sum = 0
        final_edges_sum = 0
        final_path = []
        self.pq = []

        for edge in edges:
            if edge[0] == self.start_vertex:
                heapq.heappush(self.pq, (int(edge[2]), [edge[0], edge[1]]))
        
        while self.pq:
            current_weight, current_path = heapq.heappop(self.pq)
            current_vertex = current_path[-1]

            if current_vertex == self.end_vertex:
                final_weights_sum = current_weight
                final_path = current_path
                final_edges_sum = len(current_path) - 1
                break

            for edge in self.graph_edges:
                if edge[0] == current_vertex and edge[1] not in current_path:
                    new_weight = current_weight + int(edge[2])
                    new_path = current_path + [edge[1]]
                    heapq.heappush(self.pq, (new_weight, new_path))
        
        print(f"for the shortest path algorithm travels through {final_edges_sum} edges\nwith total sum of {final_weights_sum} weights\n({') --> ('.join(final_path)})")