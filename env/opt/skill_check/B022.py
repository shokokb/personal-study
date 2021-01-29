# coding: utf-8
from functools import reduce

# M=立候補者数 N=有権者数 K=演説の回数
M, N, K = [int(m) for m in input().split()]

# 演説
groups = [N]
groups.extend([0] * M)
for i in range(K):
    a = int(input())
    for m in range(0, M + 1):
        if m != a:
            if groups[m] > 0:
                groups[a] += 1
                groups[m] -= 1
    # print(groups)
max_n = reduce(lambda x, y: max(x, y), groups[1:])
max_i = 1
for i in range(1, M + 1):
    if groups[i] == max_n:
        print(i)
