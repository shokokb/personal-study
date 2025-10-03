#coding : UTF-8

from typing import List
import unittest

class Bellmanford:
    # Time Complexity: O(k * E)
    #   - E = number of flights (edges)
    #   - k = maximum number of stops allowed
    #   For each of the k+1 rounds, we relax all E edges.
    #
    # Space Complexity: O(V)
    #   - V = number of vertices (cities)
    #   We store distances and predecessors for each vertex.
    def __init__(self, n, flights, src, dst, k):
        self.n = n
        self.vertices = range(self.n)
        self.flights = flights 
        self.src = src
        self.dst = dst 
        self.distances = {v: 0 if v == src else float('inf') for v in self.vertices}
        self.predecessors = { v: None for v in self.vertices }
        for r in range(k+1):
            temp = self.distances.copy()
            for u, v, w in self.flights:
                if self.distances[u] + w < self.distances[v] and self.distances[u] != float('inf'):
                    temp[v] = min(temp[v], self.distances[u] + w)
                    self.predecessors[v] = u
                    # print(f"round={r} k={k} {temp}")
            self.distances = temp

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        bf = Bellmanford(n, flights, src, dst, k)
        return bf.distances[dst] if bf.distances[dst] != float('inf') else -1

class TestSolution(unittest.TestCase):
    def testFindCheapestPrice(self):
        s = Solution()
        n = 4
        flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(700, s.findCheapestPrice(n, flights, src, dst, k))

        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(200, s.findCheapestPrice(n, flights, src, dst, k))

        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(500, s.findCheapestPrice(n, flights, src, dst, k))

def main():
    unittest.main()

if __name__ == "__main__":
    main()