# coding: UTF-8
from typing import List

# 選択ソート（昇順）
# Time Complexy:O(n^2)
# Space Complaxy:O(n) データの配列分
def sort(l:List[int]):
	
	if len(l) == 0:
		return []

	sorted = []
	while len(l) > 0:
		n = l.pop(0)
		if len(sorted) == 0:
			sorted.append(n)
			continue
		
		if sorted[-1] < n:
			sorted.append(n)
			continue
		
		for i, v in enumerate(sorted):
			if v > n:
				sorted.insert(i, n)
				break
		print(sorted)

	return sorted

if __name__ == "__main__":
	target = [3, 7, 4, 8, 9, 5, 6, 1, 2]
	sorted = sort(target)
	print(sorted)



