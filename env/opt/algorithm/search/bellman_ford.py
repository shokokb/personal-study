# coding: UTF-8
from typing import List

# 線形探索
# Time Complexy:O(n)
# Space Complaxy:O(1)
def search (l:List[int], t:int) -> int:
	for n in l:
		if n == t:
			return t
	return -1

if __name__ == "__main__":
	l = [5, 9, 3, 1, 2, 8, 4, 7, 6]
	t = search(l, 7)
	print(t)