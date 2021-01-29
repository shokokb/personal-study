# coding: utf-8

N, M = [int(m) for m in input().split()]
A = [int(m) for m in input().split()]
Q = int(input())
for q in range(Q):
    s, e = [int(m) for m in input().split()]
    avgv = sum(A[s-1:e]) // (e - s + 1)
    minv = min(A[s-1:e+1])
    # print("calc", s, e, M, avgv, minv)
    if avgv < M:
        for i in range(s-1, e):
            A[i] += M - avgv
print(" ".join([str(a) for a in A]))