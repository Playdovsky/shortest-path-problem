import heapq
import os
import pydot
graphviz_path = r'C:\Program Files\Graphviz\bin' 
os.environ["PATH"] += os.pathsep + graphviz_path

class ShortestPath:
    def __init__(self, vertices, num_of_edges, start_vertex, end_vertex, edges):
        self.vertices = vertices
        self.num_of_edges = num_of_edges
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.graph_edges = edges
        
        self.find_path(edges)
        self.visualize_graph()

    def find_path(self, edges):
        self.final_weights_sum = 0
        self.final_edges_sum = 0
        self.final_path = None
        self.pq = []

        for edge in edges:
            if edge[0] == self.start_vertex:
                heapq.heappush(self.pq, (int(edge[2]), [edge[0], edge[1]]))
        
        while self.pq:
            current_weight, current_path = heapq.heappop(self.pq)
            current_vertex = current_path[-1]

            if current_vertex == self.end_vertex:
                self.final_weights_sum = current_weight
                self.final_path = current_path
                self.final_edges_sum = len(current_path) - 1
                break

            for edge in self.graph_edges:
                if edge[0] == current_vertex and edge[1] not in current_path:
                    new_weight = current_weight + int(edge[2])
                    new_path = current_path + [edge[1]]
                    heapq.heappush(self.pq, (new_weight, new_path))
        
        if not self.final_path:
            print(f"No path found from ({self.start_vertex}) to ({self.end_vertex})")
            return
        
        print(f"for the shortest path algorithm travels through {self.final_edges_sum} edges\nwith total sum of {self.final_weights_sum} weights\n({') --> ('.join(self.final_path)})")

    def visualize_graph(self):
        graph = pydot.Dot(graph_type='digraph', rankdir='LR')
        
        for vertex in self.vertices:
            node = pydot.Node(str(vertex))
            graph.add_node(node)
        
        for edge in self.graph_edges:
            graph.add_edge(pydot.Edge(str(edge[0]), str(edge[1]), label=str(edge[2])))
        
        if self.final_path:
            for i in range(len(self.final_path) - 1):
                start = str(self.final_path[i])
                end = str(self.final_path[i + 1])
                graph.add_edge(pydot.Edge(start, end, color='red', penwidth='3'))
        
        graph.write_png('graph_visualization.png')
        print("Graph visualization saved to graph_visualization.png")