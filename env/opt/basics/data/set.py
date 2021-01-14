# coding: utf-8

s = set([1,1,2,2,3,4,5])
print(s)
print(list(s))
s.add(7)
print(s)
print(s.pop())
print(s.pop())
s.remove(7)
print(s)
s.clear()
print(s)
s.add(8)
print(s)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1&s2)
print(s1|s2)
print(s1-s2) #SUB
print(s1^s2) #XOR
print({1} <= {1,2})
print({2}.isdisjoint({3}))
print({2}.isdisjoint({2,3}))
