# coding: utf-8

H, W = [int(m) for m in input().split()]
flower_cnt = 0
flower_base = []
for i in range(H):
    s = list(input())
    flower_base.append(s)
    flower_cnt += s.count('#') * 4
for i in range(H):
    for j in range(W):
        if flower_base[i][j] == '#':
            if i > 0 and flower_base[i-1][j] == '#':
                flower_cnt -= 1
            if j > 0 and flower_base[i][j-1] == '#':
                flower_cnt -= 1
            if i < H - 1 and flower_base[i+1][j] == '#':
                    flower_cnt -= 1
            if j < W - 1 and flower_base[i][j+1] == '#':
                flower_cnt -= 1
print(flower_cnt)
