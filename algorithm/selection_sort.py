def selection_sort(target):
	answer = []
	for i in range(len(target)):
		# とりあえず、左端の要素を最小として初期化する
		min_value = target[i]
		min_pos = i
		# 左から見てゆき、最小のものを選択する
		for j in range(i + 1, len(target)) :
			if target[j] < min_value:
				min_pos = j
				min_value = target[j]
		# 左端が最小でなければ、スワップする
		if min_pos != i:
			target[min_pos], target[i] = target[i], target[min_pos]
	return target

target = [3, 7, 4, 8, 9, 5, 6, 1, 2]
answer = selection_sort(target)
print(answer)


