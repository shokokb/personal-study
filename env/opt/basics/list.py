# coding: UTF-8

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

