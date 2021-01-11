# coding: UTF-8
from typing import List

# バブルソート（昇順）
# Time Complexy:O(n^2)
# Space Complaxy:O(n) データの配列分
def sort (l:List[int]):
	n = len(l)
	for i in range(n):
		for j in range(n-1, i, -1):
			if l[j-1] > l[j]: l[j-1], l[j] = l[j], l[j-1]

target = [5, 9, 3, 1, 2, 8, 4, 7, 6]
sort(target)
print(target)

