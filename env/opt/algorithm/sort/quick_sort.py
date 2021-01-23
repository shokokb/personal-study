# coding: UTF-8
from typing import List

# クイックソート（昇順）
# Time Complexy:O(nlogn)
# Space Complaxy:O(n) データの配列分
def sort (l:List[int]) -> List[int]:
    if len(l) == 0:
        return []
    pivot = l[-1]
    left = []
    right = []
    for n in l[:-1]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    left = sort(left)
    right = sort(right)
    ret = []
    ret.extend(left)
    ret.append(pivot)
    ret.extend(right)
    return ret

if __name__ == "__main__":
	target = [5, 9, 3, 1, 2, 8, 4, 7, 6]
	result = sort(target)
	print(result)

