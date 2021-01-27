# coding: UTF-8
from typing import List
import math


# ベルマン・フォード法
# Time Complexy:O(mn)
def bellman_ford(start:int, edges: List) -> List:
    n = len({x for x, y, z in edges} | {y for x, y, z in edges})
    d = [math.inf] * n
    ds[start] = 0

    for i in range(n):
        update = False
        for x, y, z in edges:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負平路空間が存在する
        if i == n - 1:
            return []
    return d

if __name__ == "__main__":

    edges = []
    # 有向グラフ(始点・終点・重み)
    inputs = [[0, 1, 9], [0, 2, 2], [1, 2, 6], [1, 3, 3],
             [1, 4, 1], [2, 3, 2], [2, 5, 9], [3, 4, 5],
             [3, 5, 6], [4, 5, 3], [4, 6, 7], [5, 6, 4]]
    # 無効グラフ
    for x, y, z in inputs:
        edges.append([x, y, z])
        edges.append([y, x, z])

    result = bellman_ford(0, edges)

    print(result)