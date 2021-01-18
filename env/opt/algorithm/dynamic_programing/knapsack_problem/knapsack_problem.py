# coding: UTF-8
from typing import List

def answer (items:List[List[int]], weight:int) -> int:
	product_cnt = len(items)
	g = [[0 for m in range(weight+1)] for n in range(product_cnt + 1)]

	for i in range(1, product_cnt+1): # i番目のitem
		product_weight = items[i-1][0]
		product_value  = items[i-1][1]
		for w in range(1, weight+1):
			v1 = g[i-1][w]
			v2 = g[i-1][w-product_weight] + product_value if w-product_weight >=0 else 0
			g[i][w] = max(v1, v2)
	return g[product_cnt][weight]

if __name__ == "__main__":
    l = [[2,3],[1,2],[3,4],[2,2]]
    w = 5
    ans = answer(l,w)
    print(ans)
