# coding: utf-8
h, w, k = [int(m) for m in input().split()]
s = []
for i in range(h):
    s.append(list(input()))
max_n = 0
# 横方向
for r in range(h):
    for i in range(w - k + 1):
        n = int("".join(s[r][i:i+k]))
        if n > max_n:
            max_n = n
# 縦方向
for c in range(w):
    for r in range(h - k + 1):
        n_str = ""
        for j in range(k):
            n_str += s[r + j][c]
        n = int(n_str)
        if n > max_n:
            max_n = n
print(max_n)