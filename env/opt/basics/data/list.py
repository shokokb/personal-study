# coding: UTF-8

from collections import deque

l = [1,2,3,4,5]

# インデックス
for i in range(len(l)):
    print("index=", i)

# インデックス＆要素
for i, n in enumerate(l):
    print("enumerate", i, n)

#昇順ソート 
list_unsort = [1,5,4,2,3]
print("asc=", sorted(list_unsort))

list_unsort = [1,5,4,2,3]
list_unsort.sort()
print("asc=", list_unsort)

# 降順ソート

list_unsort = [1,5,4,2,3]
list_unsort.sort(reverse=True)
print("desc=", list_unsort)

# 逆順
list_unsort = [1,5,4,2,3]
list_unsort.reverse()
print(list_unsort)

# 逆順イテレータ
list_unsort = [1,5,4,2,3]
# print("desc=", list(reversed(list_unsort)))
for n in reversed(list_unsort):
    print(n)

# 検索
l = [1,5,4,2,3]
print("find index=", l.index(5))

# stack(List)
# 挿入
print("stack - list")
l = []
l.append(1)
l.append(2)
l.append(3)
print(l)
# pop
print("LIFO=",l.pop())

# stack(deque)
print("stack - deque")
q = deque()
q.append(1)
q.append(2)
q.append(3)
print("LIFO=", q.pop())

# queue(List)
# 挿入
print("queue - list")
l = []
l.append(1)
l.append(2)
l.append(3)
print(l)
# pop
print("FIFO=",l.pop(0))

# queue(deque)
print("queue - deque")
q = deque()
q.append(1)
q.append(2)
q.append(3)
print("FIFO=", q.popleft())