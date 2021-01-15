# coding: UTF-8

from typing import List

def sort(l:List[int]):
	for si in range(len(l)):
		target = l.pop(si)
		if si == 0:
			l.insert(si, target)
		else :
			for i, n in enumerate(l[:si]): 
				if n > target:
					l.insert(i, target)	
					break
		print(si, target, l)
		print("====")

	return

if __name__ == "__main__":
	target = [5, 9, 3, 1, 2, 8, 4, 7, 6]
	sort(target)
	print(target)

