# coding: UTF-8

import heapq

def solve():
    ans = 0
    L = [8,8,5]
    # L = list(map(lambda x: -x, L))
    heapq.heapify(L)
    print(L)    
    while L:
        if len(L) == 1:
            return ans
        l1 = heapq.heappop(L)
        l2 = heapq.heappop(L)
        ans += l1 + l2
        print("ans", l1, l2, l1 + l2)
        heapq.heappush(L, l1 + l2)

if __name__ == "__main__":
    print("solve", solve())

