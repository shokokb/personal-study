# coding: UTF-8

# 降順に並べる
def push(heap, node):
	heap.append(node)

	i = len(heap) - 1
	pi = i / 2
	while pi >= 1 :
		p = heap[pi]
		if p < node:
			heap[pi], heap[i] = heap[i], heap[pi]
			i = pi
			pi = i / 2
		else :
			break
	# print("heap", heap)
	return heap

def pop (heap):
	# 先頭のノードを取り出す
	maximum = heap.pop(1)

	# 最後のノードを先頭ノードとして挿入する
	heap.insert(1, heap[len(heap) - 1])
	heap.pop()

	i = 1
	while i < len(heap) :
		# 左ノード、右ノードを求める
		l_index = 2 * i
		r_index = 2 * i + 1
		if r_index < len(heap):
			# 左ノードの方が大きい
			if heap[l_index] > heap[r_index] :
				if heap[i] > heap[l_index]:
					# 挿入ノードが最も大きい
					break
				else :
					# 左ノードが最も大きい
					heap[l_index], heap[i] = heap[i], heap[l_index] 
					i = 2 * i 
			else :
				if heap[i] > heap[r_index]:
					# 挿入ノードが最も大きい
					break
				else : 
					# 右ノードが最も大きい
					heap[r_index], heap[i] = heap[i], heap[r_index]
					i = 2 * i + 1
		elif l_index < len(heap):
			if heap[i] > heap[l_index]:
				# 挿入ノードが最も大きい
				break;
			else :
				# 左ノードしかなく、左ノードが最も大きい
				heap[l_index], heap[i] = heap[i], heap[l_index] 
				i = 2 * i 
		else :
			break
	# print("heap, maximum", heap, maximum)
	return heap, maximum

# push
heap = ['*'] 
heap = push(heap, 5)
heap = push(heap, 2)
heap = push(heap, 7)
heap = push(heap, 3)
heap = push(heap, 6)
heap = push(heap, 1)
heap = push(heap, 4)

# pop
maximum = -1
answer = []
heap, maximum = pop(heap)
answer.append(maximum)
heap, maximum = pop(heap)
answer.append(maximum)
heap, maximum = pop(heap)
answer.append(maximum)
heap, maximum = pop(heap)
answer.append(maximum)
heap, maximum = pop(heap)
answer.append(maximum)
heap, maximum = pop(heap)
answer.append(maximum)
heap, maximum = pop(heap)
answer.append(maximum)

print(answer)
