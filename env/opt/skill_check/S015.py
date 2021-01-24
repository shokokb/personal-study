# coding: utf-8
k, s, t = [int(m) for m in input().split()]
S = ""
for i in range(k):
    if i == 0:
        S = "ABC"
    else:
        S = "A" + S + "B" + S + "C"
print(S[s-1:t])