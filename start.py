from File import File

class Start:
    def __init__(self):
        self.run()
    
    def run(self):
        try:
            file_name = input("Provide graph instructions file: ")
            file_name = "resources/" + file_name + ".txt"
            file = File(file_name)
            v, e, s, k, edges = file.read()

            print(f"\nThe number of graph...\nVertices: {v}\nEdges: {e}\nStart: {s}\nEnd: {k}\n")
            edges_length = len(edges)
            skip_next = False
            for edge in edges:
                if skip_next:
                    skip_next = False
                    continue

                next_edge = edges.index(edge) + 1
                if next_edge <= edges_length - 1 and edge[2] == edges[next_edge][2]:
                    print(f"({edge[0]}) <---- {edge[2]} ----> ({edge[1]})")
                    skip_next = True
                else:                
                    print(f"({edge[0]}) ----- {edge[2]} ----> ({edge[1]})")

        except FileNotFoundError:
            print("[ERROR] File not found. Please check the file name and try again.")
            self.run()
        except Exception as e:
            print(f"[ERROR] {e}")
            self.run()

self_start = Start()