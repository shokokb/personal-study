# coding: UTF-8

import heapq

def solve():
    # 補給回数
    ans = 0
    N = 4
    L = 25
    P = 10
    A = [10, 14, 20, 21, L]
    B = [10, 5, 2, 4, 0]
    b = []
    b = list(map(lambda x: x * -1, b))
    heapq.heapify(b)
    # 現在いる場所
    pos = 0
    # タンクの量
    tank = P
    for i in range(N):
        # 次に進む距離
        d = A[i] - pos
        # ガソリンが不足する
        while tank < d:
            if b:
                new_oil = heapq.heappop(b) * -1
                print(new_oil)
                tank += new_oil
                ans += 1
            else:
                return -1
        pos = A[i]
        tank -= d
        heapq.heappush(b, -B[i])
    return ans

if __name__ == "__main__":
    print("solve", solve())