# coding: UTF-8

def insertion_sort(target):
	# 最初の項を確定済みにする
	for i in range(len(target) - 2):
		print("i", i)
		print("confirmed", target[i])
		print("next number", target[i + 1])
		# print("未確定")
		# print(target[i:])
		for j in range(i + 1):
			print("compare", target[i + 1], target[j])
			if target[i + 1] < target[j]:
				node = target.pop(i + 1)
				target.insert(0, node)
				print("min", node, target)
				break;
		# 	else :
		# 		if j == 0:
		# 			print("確定済と比べて最も大きい場合")
		# 		elif target[j - 1] < target[i] and target[i] < target[j]:
		# 			print("間の場合")
		# 			target.insert(j, target[i])
		# 		else:
		# 			break;
		# 	print("=====")
		print("current", target)

		# # とりあえず、左端の要素を最小として初期化する
		# min_value = target[i]
		# min_pos = i
		# # 左から見てゆき、最小のものを選択する
		# for j in range(i + 1, len(target)) :
		# 	if target[j] < min_value:
		# 		min_pos = j
		# 		min_value = target[j]
		# # 左端が最小でなければ、スワップする
		# if min_pos != i:
		# 	target[min_pos], target[i] = target[i], target[min_pos]
	return target

target = [5, 3, 4, 7, 2, 8, 6, 9, 1]
answer = insertion_sort(target)
print(answer)


