# coding: UTF-8
from typing import List

# マージソート（昇順）
# Time Complexy:O(nlogn)
# Space Complaxy:O(n) データの配列分

def merge(l:List[int], r:List[int]) -> List[int]:
	ret = []
	l_i, r_i = 0, 0
	while l_i < len(l) and r_i < len(r):
		if l[l_i] <= r[r_i]:
			ret.append(l[l_i])
			l_i += 1
		else:
			ret.append(r[r_i])
			r_i += 1

	if l_i < len(l):
		ret.extend(l[l_i:])
	if r_i < len(r):
		ret.extend(r[r_i:])
	# print("merged", ret)
	return ret

def sort (l:List[int]) -> List[int]:
	if len(l) <= 1:
		return l
	
	n = len(l)
	ll = n // 2
	left = l[:ll]
	right = l[ll:]

	left = sort(left)
	right = sort(right)

	ret = merge(left, right)
	# print("l", left, "r", right, "merge", ret)

	return ret

if __name__ == "__main__":
	target = [5, 9, 3, 1, 2, 8, 4, 7, 6]
	l = sort(target)
	print(l)

