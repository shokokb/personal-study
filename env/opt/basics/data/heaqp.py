# coding: UTF-8

import heapq

if __name__ == "__main__":
    a = [1, 6, 8, 0, -1]
    heapq.heapify(a)
    heapq.heappush(a, 2)
    while a:
        print(heapq.heappop(a))
    print("len", len(a))

    print("====")

    a = [1, 6, 8, 0, -1]
    a = list(map(lambda x: x * -1, a))
    heapq.heapify(a)
    heapq.heappush(a, 2 * -1)
    while a:
        print(heapq.heappop(a) * -1)
    print("len", len(a))


