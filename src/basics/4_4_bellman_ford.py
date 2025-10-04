#coding : UTF-8

class Bellmanford:
    def __init__(self, vertices, edges, start):
        self.vertices     = vertices
        self.edges        = edges
        self.start        = start
        self.distances    = {v: float('inf') for v in vertices}
        self.predecessors = {v: None for v in vertices}
        self.distances[self.start] = 0
        for i in range(len(self.vertices)-1):
            temp = self.distances.copy()
            for u, v, w in self.edges:
                if self.distances[u] + w < self.distances[v] and self.distances[u] != float('inf'):
                    temp[v] = min(self.distances[u] + w, temp[v])
                    self.predecessors[v] = u
            self.distances = temp

    def get_shortest_path(self, goal):
        path = []
        v = goal
        while v is not None:
            path.append(v)
            # print(v, path)
            v = self.predecessors[v]
        path.reverse()
        return path

    def get_all_paths(self):
        result = {}
        for v in self.vertices:
            result[v] = (self.distances[v], self.get_shortest_path(v))
        return result
    
    def has_negative_cycle(self):
        for u, v, w in self.edges:
            if self.distances[u] + w < self.distances[v]:
                return True
        return False

def main():
    start = "A"
    vertices = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", -2),
        ("A", "C", 4)
    ]
    bf = Bellmanford(vertices, edges, start)
    result = bf.has_negative_cycle()
    print("negative cycle" if result else "not negative cycle")
    paths = bf.get_all_paths()
    print(paths)

if __name__ == "__main__":
    main()