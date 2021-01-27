# coding: UTF-8
from typing import List
import math


# ダイクストラ法
# Time Complexy:O(mn)
def bellman_ford(start: int, edges: List) -> List:
    n = len({x for x, y, z in edges} | {y for x, y, z in edges})
    d = [math.inf] * n
    d[start] = 0
    applied = [start]

    while applied:
        # 最小のノードを見つける
        p1 = applied[0]
        for i in applied:
            if d[i] < d[p1]:
                p1 = i
        applied.remove(p1)
        # 隣のノードを更新する
        for x, y, z in edges: #O(m)
            if x == p1:
                if d[y] > d[x] + z:
                    d[y] = d[x] + z
                    applied.append(y)
            if y == p1:
                if d[x] > d[y] + z:
                    d[x] = d[y] + z
                    applied.append(x)
    return d


if __name__ == "__main__":

    edges = []
    # 有向グラフ(始点・終点・重み)
    inputs = [[0, 1, 2], [0, 2, 5], [1, 2, 6], [1, 3, 1], [1, 4, 3], [2, 5, 8],
              [4, 6, 9], [5, 6, 7]]
    # 無向グラフ
    for x, y, z in inputs:
        edges.append([x, y, z])
        edges.append([y, x, z])

    result = bellman_ford(0, edges)

    print(result)