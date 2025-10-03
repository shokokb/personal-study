#coding : UTF-8

def bellman_ford(vertices, edges, start) :
    distances = {v: float('inf') for v in vertices}
    predecessors = {v: None for v in vertices}

    distances[start] = 0
    for i in range(len(vertices)-1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u
        print(distances)

    return distances, predecessors   

def get_shortest_path(predecessors, goal):
    path = []
    v = goal
    while v is not None:
        path.append(v)
        # print(v, path)
        v = predecessors[v]
    path.reverse()
    return path

def main():
    start = "A"
    vertices = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", -2),
        ("A", "C", 4)
    ]

    distances, predecessors = bellman_ford(vertices, edges, start)
    
    print(distances["C"])
    # A to C
    path = get_shortest_path(predecessors, "C")
    print(path)

if __name__ == "__main__":
    main()