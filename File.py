class File:
    def __init__(self, name):
        self.name = name
    
    def read(self):
        with open(self.name, 'r') as file:
            lines = file.readlines()

            graph_config_vars = lines[0].strip().split(' ')
            v = graph_config_vars[0]
            e = graph_config_vars[1]
            s = graph_config_vars[2]
            k = graph_config_vars[3]

            edges = []
            for line in lines[1:]:
                edge = line.strip().split(' ')
                edges.append((edge[0], edge[1], edge[2]))
        
        return v, e, s, k, edges
