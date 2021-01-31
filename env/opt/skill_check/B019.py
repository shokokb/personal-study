# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N, K = [int(m) for m in input().split()]
a = []
for i in range(N):
    a.append([int(m) for m in input().split()])
    
w = len(a[0]) // K
h = N // K

b = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        sumv = 0
        for k in range(K):
            # print(a[K*i+k][K*j:K*(j+1)])
            sumv += sum(a[K*i+k][K*j:K*(j+1)])
        avgv = sumv // (K**2)
        b[i][j] = str(avgv)
        # print(i, j, avgv)
for i in range(h):
    print(" ".join(b[i]))
