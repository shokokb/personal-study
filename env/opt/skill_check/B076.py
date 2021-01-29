# coding: utf-8
# N=種類, Q=クエリ数
N, Q = [int(m) for m in input().split()]
# a[i][0]=値段 a[i][1]=在庫
a = [[int(m) for m in input().split()] for i in range(N)]
# クエリ
for t in range(Q):
    input_line = input()
    q = input_line.split()[0]
    # c[i]=販売個数
    c = [int(m) for m in input_line.split()[1:]]
    if q == "buy":
        cost = 0
        result = all(a[i][1] >= c[i] for i in range(N))
        if result:
            for i in range(N):
                a[i][1] -= c[i]
                cost += a[i][0] * c[i]
            print(cost)
        else:
            print(-1)
    else:
        for i in range(N):
            a[i][1] += c[i]
