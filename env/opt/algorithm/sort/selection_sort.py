from typing import List

# バブルソート（昇順）
# Time Complexy:O(n^2)
# Space Complaxy:O(n) データの配列分
def selection_sort(l:List[int]):
	n = len(l)
	for i in range(n):
		mp, mv = i, l[i]
		for j in range(i+1, n):
			if mv > l[j]: mp, mv = j, l[j]
		l[i], l[mp] = l[mp], l[i]

target = [3, 7, 4, 8, 9, 5, 6, 1, 2]
selection_sort(target)
print(target)



