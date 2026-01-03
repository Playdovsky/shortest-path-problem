import os
import pydot
# Windows has problems with identifying graphviz installation path. On Linux it works fine without path.
graphviz_path = r'C:\Program Files\Graphviz\bin' 
os.environ["PATH"] += os.pathsep + graphviz_path

class Visualize:
    def __init__(self, vertices, graph_edges, final_path):
        self.vertices = vertices
        self.graph_edges = graph_edges
        self.final_path = final_path
        
        self.visualize_graph()
    
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