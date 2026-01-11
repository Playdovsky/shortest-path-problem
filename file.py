class File:
    def __init__(self, name):
        self.name = name
    
    def read(self):
        with open(self.name, 'r') as file:
            lines = file.readlines()

            graph_config_vars = lines[0].strip().split(' ')
            v = graph_config_vars[0] # number of vertices
            e = graph_config_vars[1] # number of edges
            s = graph_config_vars[2] # start vertex
            k = graph_config_vars[3] # end vertex

            edges = []
            for line in lines[1:]:
                edge = line.strip().split(' ')
                # 0: start vertex, 1: end vertex, 2: weight
                edges.append((edge[0], edge[1], edge[2]))
        
        return v, e, s, k, edges