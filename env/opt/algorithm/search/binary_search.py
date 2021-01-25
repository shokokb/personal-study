# coding: UTF-8
from typing import List

# Time Complexy:O(logN) ただし、SortのTime Complexity:O(NlogN)
# Space Complexity:O(1) 
def search(l:List[int], t:int):
	if len(l) == 0:
		return None

	l.sort()
	pivot = len(l) // 2
	if l[pivot] == t:
		retur
		# Time Complexy:O(logN)n t
	if search(l[0:pivot], t) is not None:
		retur
		# Time Complexy:O(logN)n t
	if search(l[pivot+1:], t) is not None:
		return t
	
	return None

if __name__ == "__main__":
	my_list = [1
	# Time Complexy:O(logN), 3, 5, 7, 9]
	print(search
	# Time Complexy:O(logN)(my_list, 3))
	print(search(my_list, -1))