# coding: utf-8

# setオブジェクトの生成: {}, set()
# s = set([1,1,2,2,3,4,5])
s = {1,1,2,2,3,4,5}

print(s)

print(list(s))

print(tuple(s))

# 集合内包表記
s = {i for i in range(6)}

# 集合の要素数: len()関数
print("len=", len(s))

# 集合に要素を追加: add()
s.add(7)
print("add=", s)

# 集合から要素を削除: 
# discard() : 指定の要素がない場合、エラーとならない
# remove()　：指定の要素がない場合、エラーとなる
# pop()　　　：ランダムな要素を削除する
s.discard(6)
print("discard=", s)
#s.remove(8)
s.remove(5)
print("remove=", s)
n = s.pop()
print("pop=", n, s)

# clear()
s.clear()
print("clear=", s)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
# 和集合（合併、ユニオン）: |演算子, union()
print(s1|s2)
# 積集合（共通部分、交差、インターセクション）: &演算子, intersection()
print(s1&s2)
# 差集合: -演算子, difference()
print(s1-s2) #SUB
# 対称差集合: ^演算子, symmetric_difference()
print(s1^s2) #XOR
# 部分集合か判定: <=演算子, issubset()
print({1} <= {1,2})
# 上位集合か判定: >=演算子, issuperset()
print({1,2,3} >= {2,3})
# 互いに素か判定: isdisjoint()
print({2}.isdisjoint({3}))
print({2}.isdisjoint({2,3}))
