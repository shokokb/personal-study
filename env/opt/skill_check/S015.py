# coding: utf-8

from collections import defaultdict

k, s, t = [int(m) for m in input().split()]
dict_abc = defaultdict(lambda:None)
dict_abc[1] = "ABC"
def abc(k):
    if k == 1:
        return dict_abc[1]
    if dict_abc[k - 1] is None:
        dict_abc[k - 1] = abc(k - 1)
    dict_abc[k] = "A" + dict_abc[k - 1] + "B" + dict_abc[k - 1] + "C"
    return dict_abc[k]
for i in range(k):
    S = abc(k)
print(S[s-1:t])
# 最初のA = 0
#  012 => 3
# "ABC"
#  0     123     4     567     8 => 9
# "A" + "ABC" + "B" + "ABC" + "C"