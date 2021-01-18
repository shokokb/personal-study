# coding: UTF-8
from typing import List

def answer (str1:str, str2:str) -> int:
    s1, s2 = list(str1), list(str2)
    n1, n2 = len(s1), len(s2)
    s1.insert(0, '')
    s2.insert(0, '')
    
    g = [[0 for m in range(n2+1)] for n in range(n1+1)]

    for i1 in range(1, n1+1):
        for i2 in range(1, n2+1):
            if s1[i1] == s2[i2]:
                g[i1][i2] = g[i1-1][i2-1]+1
            else:
                g[i1][i2] = 0
    #print(g)
    return g[-1][-1]

if __name__ == "__main__":
    ans = answer("abcd","becd")
    print(ans)
