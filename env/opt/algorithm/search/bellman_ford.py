# coding: UTF-8
from typing import List
from collections import deque
from collections import defaultdict
import math


# ベルマン・フォード法
# Time Complexy:O(mn)
def search(start: str, end: str, edges: List[tuple]) -> int:
    tmp_edges = edges.copy()
    change = True

    # 距離
    distance = {
        c: math.inf
        for c in [chr(c) for c in range(ord(start),
                                        ord(end) + 1)]
    }
    distance[start] = 0

    queue = deque()
    queue.append(start)

    while change:
        change = False
        # O(m)
        while tmp_edges:
            point_from = queue.popleft()
            cur_edges = list(filter(lambda edge: edge[0] == point_from, tmp_edges))
            for edge in cur_edges:
                point_to = edge[1]
                if distance[point_from] + edge[2] < distance[point_to]:
                    distance[point_to] = distance[point_from] + edge[2]
                    change = True
                tmp_edges.remove(edge)
                queue.append(point_to)
        print(distance)

    return distance[end]


if __name__ == "__main__":

    edges = [('A', 'B', 9), ('A', 'C', 2), ('B', 'C', 6), ('B', 'D', 3),
             ('B', 'E', 1), ('C', 'D', 2), ('C', 'F', 9), ('D', 'E', 5),
             ('D', 'F', 6), ('E', 'F', 3), ('E', 'G', 7), ('F', 'G', 4),
             ('B', 'A', 9), ('C', 'A', 2), ('C', 'B', 6), ('D', 'B', 3),
             ('E', 'B', 1), ('D', 'C', 2), ('F', 'C', 9), ('E', 'D', 5),
             ('F', 'D', 6), ('F', 'E', 3), ('G', 'E', 7), ('G', 'F', 4)]

    result = search('A', 'G', edges)

    print(result)