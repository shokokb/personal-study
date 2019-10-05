# coding: UTF-8

# バブルソート（昇順）
def bubble_sort (target) :
	for i in range(0, len(target)):
		back_range = reversed(range(i + 1, len(target)))
		for j in list(back_range):
			# 後ろから隣り合う2つを比べて最も小さな数を左に格納してゆく
			if target[j - 1] > target[j]:
				target[j], target[j - 1] = target[j - 1], target[j]
	return target

target = [5, 9, 3, 1, 2, 8, 4, 7, 6]
expected = bubble_sort(target)
print(expected)

