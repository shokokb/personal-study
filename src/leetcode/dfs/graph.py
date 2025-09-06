from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # 無向グラフ

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            v = stack.pop()
            if v not in visited:
                print(v, end=" ")
                visited.add(v)
                # 逆順で追加すると自然な順序になる
                for neighbor in reversed(self.graph[v]):
                    if neighbor not in visited:
                        stack.append(neighbor)

# 使用例
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("DFS recursive:")
g.dfs_recursive(0)  # 0 1 3 4 2 5

print("\nDFS iterative:")
g.dfs_iterative(0)  # 0 1 3 4 2 5